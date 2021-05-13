N = int(input())
A = list(map(int,input().split()))
B = []
for k in range(N):
    B.append(A[k]-(k+1))
t = sorted(B)[N//2]
ans = 0
for k in range(N):
    ans += abs(A[k]-(t+k+1))
print(ans)
