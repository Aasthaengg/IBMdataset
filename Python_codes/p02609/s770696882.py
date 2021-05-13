N=int(input())
X=input()
a=int(X,2)

def popcount(x):
  return bin(x).count("1")
p=X.count('1')

pl=a%(p+1)
if p!=1:
  mi=a%(p-1)

def f(x):
  if x==0:
    return 1
  else:
    return f(x%popcount(x))+1

for i in range(N):
  if X[i]=='0':
    b=pl
    b+=pow(2,N-i-1,p+1)
    b%=p+1
  else:
    if p!=1:
      b=mi
      b-=pow(2,N-i-1,p-1)
      b%=p-1
    else:
      print(0)
      continue
  print(f(b))
