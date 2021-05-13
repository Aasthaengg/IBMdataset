k,s=input().split()
k=int(k)
s=int(s)
cnt=0
for x in range(k+1):
  for y in range(k+1):
    z=s-x-y
    if z>=0 and z<=k:
      cnt+=1
print(cnt)