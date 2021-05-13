n=int(input())
l=[1,2,4,8,16,32,64,128]
ans=0
for i in l:
  if n < i:
    print(ans)
    exit()
  ans=i
