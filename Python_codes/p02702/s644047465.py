from collections import defaultdict
S=input()
D=defaultdict(int)
D[0]=1
n=0
i=0
a=[0]*len(S)
b=1
for s in S[::-1]:
  n+=int(s)*b
  a[i]=n%2019
  i+=1
  b=(b*10)%2019


for i in range(len(a)):
  D[a[i]]+=1

ans=sum([i*(i-1)//2 for i in D.values()])
print(ans)  