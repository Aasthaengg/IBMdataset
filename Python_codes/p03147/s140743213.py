n = int(input())
h = list(map(int, input().split()))

count = 0
while not all([x <= 0 for x in h]):
    while h[0] == 0:
        del h[0]
    subcount = 0
    for i in range(len(h)-1):
        if (h[i] > 0 or h[i+1] > 0) and h[i]*h[i+1] == 0:
            subcount += 1
    h = [x - 1 if x - 1 >= 0 else 0 for x in h]
    subcount = subcount // 2 + 1
    count += subcount

print(count)
