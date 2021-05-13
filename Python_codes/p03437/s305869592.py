x,y=map(int,input().split())
for i in range(10**5):
  if (x*i)%y!=0:
    print(x*i)
    exit()
print(-1)