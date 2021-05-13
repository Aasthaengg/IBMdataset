def waru(k,l):
  if k%l==0:
    return k//l
  else:
    return (k//l)+1
A=0
B=0
N=int(input())
for i in range(N):
  a,b=map(int,input().split())
  if a>=A and b>=B:
    A,B=a,b
  elif a>=A and b<B:
    A,B=a*waru(B,b),b*waru(B,b)
  elif a<A and b>=B:
    A,B=a*waru(A,a),b*waru(A,a)
  else:
    c=max(waru(A,a),waru(B,b))
    A,B=a*c,b*c
print(A+B)