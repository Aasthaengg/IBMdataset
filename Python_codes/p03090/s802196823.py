N = int(input())
ans = [[j for j in range(i+1,N)]for i in range(N)]
for i in range(N):
    if len(ans[i]) >= N%2+i+1:
        ans[i][-(N%2+i+1)] = -1
out = []
for i in range(N):
    for j in ans[i]:
        if j >= 0:
            out.append([i+1,j+1])
print(len(out))
for i,j in out:
    print(i,j)