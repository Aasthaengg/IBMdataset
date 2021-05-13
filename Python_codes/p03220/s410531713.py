a=int(input())
b,c=input().split()
b=int(b)
c=int(c)
l=list(map(int,input().split()))
for i in range(a):
  l[i]=abs(c-(b-l[i]*0.006))
for i in range(a):
  if l[i]==min(l):
    print(i+1)