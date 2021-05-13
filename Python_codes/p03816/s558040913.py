n=int(input())
a=list(map(int,input().split()))
i=len(a)
s=set(a)
j=len(s)
if (i-j)%2==0:
  print(n-(i-j))
else:
  print(n-(i-j+1))
