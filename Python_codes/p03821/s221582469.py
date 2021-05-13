n=int(input())
ab=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  ab.append(tmp)
tmp=0
for a,b in ab[::-1]:
  a+=tmp
  if a%b!=0:
    tmp+=(b-a%b)
print(tmp)