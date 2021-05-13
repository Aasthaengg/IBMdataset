import sys
mina=10**10
def waru(a,b):
  if a%b==0:
    return a//b
  else:
    return (a//b)+1
N,H=map(int,input().split())
A=list()
B=list()
for i in range(N):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
ma=max(A)
ind=A.index(ma)
B=[i for i in B if i>ma]
B=sorted(B,reverse=True)
cou=1
s=0
for i in range(len(B)):
  s+=B[i]
  if H<=s:
    print(i+1)
    sys.exit()
H=H-s
print(len(B)+waru(H,ma))