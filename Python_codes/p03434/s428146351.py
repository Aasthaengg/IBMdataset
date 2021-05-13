n=int(input())
li=list(map(int,input().split()))
newli=sorted(li)
gu=[]
ki=[]
for i in range(n):
  if i%2==0:
    gu.append(newli[-(i+1)])
  else:
    ki.append(newli[-(i+1)])
print(sum(gu)-sum(ki))
