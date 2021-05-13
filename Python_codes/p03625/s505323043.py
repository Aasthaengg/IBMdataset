n=int(input())
a=list(map(int,input().split()))
a.sort()
l=[]
i=0
while i<n-1:
  if a[i]==a[i+1]:
    l.append(a[i])
    i+=2
  else:
    i+=1
l.reverse()
if len(l)<2:
  print(0)
else:
  print(l[0]*l[1])