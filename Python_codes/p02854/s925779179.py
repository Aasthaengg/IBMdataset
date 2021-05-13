N=int(input())
L=list(map(int,input().split()))
suml=sum(L)
l,ll,i=L[0],0,0
while l<suml/2:
  i+=1
  ll=l
  l+=L[i]

key=min(l-suml/2,suml/2-ll)
print(int(key*2))