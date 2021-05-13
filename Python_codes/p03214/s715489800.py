n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/len(a)
minv=sum(a)
mini=0
for i in range(len(a)):
  if abs(a[i]-ave)<minv:
    minv=abs(a[i]-ave)
    mini=i
print(mini)