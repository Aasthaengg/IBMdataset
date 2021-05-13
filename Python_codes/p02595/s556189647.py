n,d = map(int,input().split())
ans =0

for i in range(n):
  xi,yi = map(int,input().split())
  if d**2 >= xi**2+yi**2 :
    ans +=1
print(ans)