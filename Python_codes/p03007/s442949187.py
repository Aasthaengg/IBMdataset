n,a=int(input()),sorted(list(map(int,input().split())))
mn,mx=a[0],a[-1]
for i in a[1:-1]:
  if i<0:mx-=i
  else:mn-=i
print(mx-mn)
mn,mx=a[0],a[-1]
for i in a[1:-1]:
  if i<0:print(mx,i);mx-=i
  else:print(mn,i);mn-=i
print(mx,mn)
