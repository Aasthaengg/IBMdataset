n = int(input())
out = []
ans = []
if n%2 == 0:
    for i in range(1,n//2+1):
        out.append([i, n-i+1])
else:
    for i in range(1, n//2+1):
        out.append([i,n-i])
for i in range(1,n+1):
    for j in range(i+1, n+1):
        if [i,j] not in out:
            ans.append([i,j])
print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
