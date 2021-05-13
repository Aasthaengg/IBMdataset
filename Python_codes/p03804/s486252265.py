n, m = map(int, input().split())
a = [input() for i in range(n)]
b = "".join([input() for i in range(m)])
ans = "No"
for i in range(n-m+1):
    for j in range(n-m+1):
        s = ""
        for k in range(m):
            s+=a[i+k][j:j+m]
        if s==b:
            ans = "Yes"
print(ans)