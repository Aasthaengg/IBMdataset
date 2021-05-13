N,K = map(int, input().split())
H = list(map(int, input().split()))
a = sorted(H,reverse=True)
if(K>0):
  for i in range(min(K,N)):
    a[i]=0
print(sum(a))