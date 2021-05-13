import itertools

n,q=map(int,input().split())
s=input()
lst=[0]*(n-1)

for i in range(n-1):
  if s[i:i+2]=='AC':
    lst[i]+=1
    
lst=list(itertools.accumulate(lst))
lst=[0]+lst

for i in range(q):
  s,t=map(int,input().split())
  print(lst[t-1]-lst[s-1])