N = int(input())
ans = []
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if N % 2 == 0 and i+j == N+1: continue
        if N % 2 == 1 and i+j == N: continue
        ans.append([i,j])
print(len(ans))
for a in ans:
    print(a[0],a[1])