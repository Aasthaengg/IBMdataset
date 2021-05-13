N,K=map(int,input().split())
t=[0]*N
for i in range(N): t[i]=int(input())
t.sort(key=int)
print(min(t[i+K-1]-t[i] for i in range(N-K+1)))