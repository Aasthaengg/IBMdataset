A,B,K=list(map(int,input().split()))
gcd=[]
C=min(A,B)
for i in range(1,C+1):
  if A%i==0 and B%i==0:
    gcd.append(i)
print(gcd[-K])