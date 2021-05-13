a,b,c=map(int,sorted(list(map(int,input().split()))))
cnt=0
while True:
  if a==b==c:break
  elif a==b:
    cnt+=c-a
    break
  else:
    a,b,c=map(int,sorted([a+2,b,c]))
    cnt+=1
print(cnt)