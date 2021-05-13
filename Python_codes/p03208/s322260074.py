N,K=map(int,input().split())
h=[0]*N
for i in range(N):
  h[i]=int(input())
h.sort()
diff=[]
for i in range(N-K+1):
  diff.append(h[i+K-1]-h[i])
print(min(diff))