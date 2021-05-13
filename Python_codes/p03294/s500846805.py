n = int(input())
a = list(map(int,input().split()))
m =1
for i in range(n):
    m *= a[i]
mod = m-1

ans = 0
for i in range(n):
    tmp = mod % a[i]
    ans += tmp
print(ans)