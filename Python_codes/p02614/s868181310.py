h,w,k=map(int,input().split())
c=[list(input()) for i in range(h)]
a=0

for i in range(1<<h+w):
  x=0
  for j in range(h):
    for l in range(w):
      if i>>j & 1 and i>>l+h & 1:
        if c[j][l]=="#":
          x+=1
  if x==k:
    a+=1
print(a)    