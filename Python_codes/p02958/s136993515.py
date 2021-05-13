n = int(input())
l = [i - 1 for i in map(int, input().split())]
cnt = 0
for j, k in enumerate(l):
    if j != k:
        cnt += 1
if cnt == 0 or cnt == 2:
    print('YES')
else:
    print('NO')