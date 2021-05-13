N=int(input())
a=list(map(int,input().split()))
s=[]

def count(k):
  p=0
  while k % 2**p==0:
    p+=1
  return p-1
	
for i in range(N):
  s.append(count(a[i]))

print(min(s))