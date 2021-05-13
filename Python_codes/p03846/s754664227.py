n,*a=map(int,open(0).read().split())
a=sorted(a)
cnt=0
if len(a)%2==0:
  for i in range(1,len(a),2):
    if [i,i]==a[i-1:i+1]:
      cnt+=1
    else:
      cnt=-10**5-1
else:
  if a[0]==0:
    for i in range(2,len(a),2):
      if [i,i]==a[i-1:i+1]:
        cnt+=1
      else:
        cnt=-10**5-1
  else:
    cnt=-10**5-1
print((2**cnt)%(10**9+7) if cnt>=0 else 0)