N,K = map(int,input().split())
tree = sorted([int(input())for i in range(N)])
d = 10**18  


for i in range(N-K+1):
  d = min(d,tree[i+K-1]-tree[i])
print(d)