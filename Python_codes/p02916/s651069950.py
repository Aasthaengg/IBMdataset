n = int(input())
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))
ans = 0
tmp = 0
for i in range(1,n+1):
    ans += b[a[i]]
    if tmp==a[i]-1:
        ans += c[tmp]
    tmp = a[i]
print(ans)
