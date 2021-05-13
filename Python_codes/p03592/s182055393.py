#総当たりできる
n,m,k = map(int, input().split( ))

ans = set()
for i in range(n+1):
    for j in range(m+1):
        ans.add(i*j+(n-i)*(m-j))###
if k in ans:
    print("Yes")
else:
    print("No")