n,k = map(int,input().split())
a = list(map(int,input().split()))

gen=10**9+7

count=0
for i in range(n):
  for j in range(i+1,n):
    if a[i]>a[j]:
      count+=1

kaburi = 0
sorta=sorted(a)
scnt=0
for i in range(n-1):
  if sorta[i]==sorta[i+1]:
    scnt+=1
  if sorta[i]!=sorta[i+1]:
    kaburi+=scnt*(scnt+1)//2
    scnt=0
kaburi+=scnt*(scnt+1)//2

print((k*count+(n*(n-1)//2-kaburi)*k*(k-1)//2)%gen)