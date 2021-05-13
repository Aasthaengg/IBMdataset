N=int(input())
A,B=map(int,input().split())
for i in range(N-1):
  a,b=map(int,input().split())
  if a==b:
    if A<B:
      A=B
    else:
      B=A
    
  else:
    if a/b > A/B:
      # Bに対していく
      if B%b!=0:
        plus=b-(B%b)
        B+=plus
      A=(B*a)//b
    else:
      # Aに足していく
      if A%a!=0:
        plus=a-(A%a)
        A+=plus
      B=(A*b)//a

print(A+B)  