n=int(input());l=[[]for _ in[0]*n];c=[1]+[0]*(n-2)+[-1];q=[0,n-1]
for _ in[0]*q[1]:a,b=map(int,input().split());l[a-1]+=[b-1];l[b-1]+=[a-1]
while q:
  p=[]
  for i in q:
    for j in l[i]:
      if c[j]==0:c[j]=c[i];p+=[j]
  q=p
print("FSennunkeec"[sum(c)<1::2])