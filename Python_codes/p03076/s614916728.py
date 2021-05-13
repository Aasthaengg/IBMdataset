a=[int(input()) for i in range(5)]
sa=[0]*5
l=[0]*5
for i in range(5):
  l[i]=10*((a[i]+9)//10)
  sa[i]=10*((a[i]+9)//10)-a[i]
print(sum(l)-max(sa))