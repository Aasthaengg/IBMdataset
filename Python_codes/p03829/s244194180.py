k=0
def s(a):
  return min(a*A,B)
N,A,B=map(int,input().split())
L=list(map(int,input().split()))
for i in range(N-1):
  k+=s(L[i+1]-L[i])
print(k)