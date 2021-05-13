n,m = map(int, input().split())
a = list(map(int, input().split()))
syukudai = 0

for i in range(m):
    syukudai += a[i]
    if syukudai > n:
        print(-1)
        break
else:
    print(n-syukudai)