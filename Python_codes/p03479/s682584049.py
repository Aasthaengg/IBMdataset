X,Y = map(int,input().split())
ans = 1
x = X

for n in range(Y):
  if x*2<=Y:
    ans+=1
    x*=2
  else:
    print(ans)
    exit()