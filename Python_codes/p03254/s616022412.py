N,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
if sum(a) == x:
    print(N)
    exit()
if sum(a) <= x:
    print(N-1)
    exit()
ans = 0
for i in range(N):
    ans += a[i]
    if ans == x:
        print(i+1)
        exit()
    if ans > x:
        print(i)
        exit()