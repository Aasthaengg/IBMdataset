def main(n,k,a):
  for _ in range(k):
    b=[0]*(n+1)
    x=0
    for i,j in enumerate(a):
      b[max(0,i-j)]+=1
      b[min(n,i+j+1)]-=1
    for i in range(n):
      b[i+1]+=b[i]
      if b[i]==n:
        x+=1
    a=b
    if x==n:
      break
  return a
N,K,*A=map(int,open(0).read().split())
r=main(N,K,A)
print(*r[:-1])