from collections import Counter
n=int(input())
a=list(Counter(list(map(int,input().split()))).items())
ans=0
for i in range(len(a)):
  if a[i][0]<a[i][1]:
    ans+=a[i][1]-a[i][0]
  elif a[i][0]>a[i][1]:
    ans+=a[i][1]
print(ans)

