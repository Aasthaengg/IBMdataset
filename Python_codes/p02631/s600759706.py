n = int(input())
a = list(map(int,input().split()))
ans = []
tmp = a[0]
for i in range(1,n):
    tmp = tmp^a[i]
ans = ''
for i in range(n):
    ans += str(int(tmp^a[i]))+' '
print(ans[:-1])