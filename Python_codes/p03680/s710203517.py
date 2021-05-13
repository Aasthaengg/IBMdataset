n=int(input());a=[int(input()) for _ in range(n)]
num,cnt=0,1
while a[num]!=2:
  num=a[num]-1
  cnt+=1
  if cnt==n:
    print(-1);exit()
print(cnt)