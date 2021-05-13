N = int(input())
h = [int(x) for x in input().split()]
count = 0
con = 0
while True:
    for i in range(N):
        if h[i] > 0:
            h[i] -= 1
            con = 1
        elif h[i] <= 0:
            if con == 1:
                count += 1
            con = 0
    if con == 1:
        count += 1
    con = 0
    if not any(h):
        break

print(count)
