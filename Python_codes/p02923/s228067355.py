n = int(input())
h = list(map(int, input().split()))
move = []
count = 0
tmp = h[0]
for i in range(1, n):
    if h[i] <= tmp:
        count += 1
        tmp = h[i]
    else:
        move.append(count)
        tmp = h[i]
        count =0
move.append(count)
print(max(move))