N = int(input())
ans = []
if N%2 == 0:
    for k in range(1,N):
        for l in range(k+1,N+1):
            if k+l != N+1:
                ans.append([k,l])
else:
    for k in range(1,N):
        for l in range(k+1,N+1):
            if k+l != N:
                ans.append([k,l])
print(len(ans))
for e in ans:
    print(*e)
