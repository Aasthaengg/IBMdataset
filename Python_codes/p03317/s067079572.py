N,K=map(int,input().split())
List = list(map(int, input().split()))
k=K-1
n = (N-1)/k
nn = int(n)
if n-nn > 0:
  nn = nn+1
print(nn)