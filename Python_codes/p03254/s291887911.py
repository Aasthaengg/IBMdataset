n, x = map(int, input().split())
A = sorted([int(i) for i in input().split()])
# print(A)
cnt = 0
for e in A:
    if e <= x:
        x = x - e
        cnt += 1
if cnt == n and x > 0:
    print(cnt-1)
else:
    print(cnt)
