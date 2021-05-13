N=int(input())
L=list(map(int,input().split()))
s=len(set(L))
if s%2==0:
  s-=1
print(s)