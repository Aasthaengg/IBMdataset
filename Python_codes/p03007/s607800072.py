n=int(input())
a=list(map(int,input().split()))
a.sort()
import bisect 
if a[0]*a[-1]<0:
  print(abs(sum([abs(x) for x in a])))
  tmp=a[0]
  t=bisect.bisect_right(a,0)
  for i in range(t+1,n):
    print(tmp,a[i])
    tmp-=a[i]
  a[0]=tmp
  tmp=a[t]
  for i in range(t-1):
    print(tmp,a[i])
    tmp-=a[i]
  print(tmp,a[t-1])

elif a[0]==0:
  print(abs(sum([abs(x) for x in a])))
  tmp=a[0]
  for i in range(1,n-1):
    print(tmp,a[i])
    tmp-=a[i]
  print(a[-1],tmp)
elif a[-1]==0:
  print(abs(sum([abs(x) for x in a])))
  tmp=a[-1]
  for i in range(n-2,-1,-1):
    print(tmp,a[i])
    tmp-=a[i]

elif a[0]>0:
  print(sum(a)-2*a[0])
  tmp=a[0]
  for i in range(1,n-1):
    print(tmp,a[i])
    tmp-=a[i]
  print(a[-1],tmp)
else:
  print(abs(sum(a))+2*a[-1])
  tmp=a[-1]
  for i in range(n-2,-1,-1):
    print(tmp,a[i])
    tmp-=a[i]
