n,k = map(int,input().split())
x_ls = list(map(int, input().split()))
ans = float('inf')
for i in range(n-k+1):
    if x_ls[i+k-1] < 0:
        ans = min(ans, abs(x_ls[i]))
    elif x_ls[i] < 0 and x_ls[i+k-1] >= 0:
        near = min(abs(x_ls[i]),abs(x_ls[i+k-1]))
        far = max(abs(x_ls[i]),abs(x_ls[i+k-1]))
        ans = min(ans, 2 * near + far)
    elif x_ls[i] >= 0:
        ans = min(ans, x_ls[i+k-1])
print(ans)