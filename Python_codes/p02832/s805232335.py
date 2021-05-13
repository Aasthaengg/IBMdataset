n=int(input())
c=list(map(int, input().split()))

ans = 1
a = 0

for i in range(n):
    if c[i] != ans :
        a += 1
    if c[i] == ans:
        ans += 1

if ans == 1 and a != 0:
    print(-1)
else:
    print(a)