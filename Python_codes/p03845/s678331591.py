N=int(input())
L=list(map(int,input().split()))
Q=int(input())
c=sum(L)
for i in range(Q):
  a,b=map(int,input().split())
  print(c-(L[a-1]-b))