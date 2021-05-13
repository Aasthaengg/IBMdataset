a,b,c=list(map(int,input().split()))
n=0
H=[]
while True:
  S=[a,b,c]
  if S in H:
    print("-1")
    exit()
  H.append(S)
  if a%2!=0 or b%2!=0 or c%2!=0:
    print(n)
    exit()
  else:
    A=a/2
    B=b/2
    C=c/2
    a=int(B+C)
    b=int(A+C)
    c=int(A+B)
    n+=1