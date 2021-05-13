N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
data=[]; ans=0
for i in range(N): data.append(V[i]-C[i])
for i in range(N): ans += 0 if data[i] <= 0 else data[i]
print(ans)