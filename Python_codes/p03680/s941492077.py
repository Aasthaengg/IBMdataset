N = int(input())
A = [int(input()) for i in range(N)]

G = [1]
for i in range(N):
    G.append(A[G[-1]-1])
    
ans = 0
for i in range(N+1):
    if G[i]==2:
        break
    ans += 1
else:
    ans = -1
    
print(ans)