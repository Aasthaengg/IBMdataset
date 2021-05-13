a,b,x=map(int,input().split())
 
flag=False
for i in range(0,b+1):
    if a+i==x:
        flag = True
        break
 
if flag:
    print("YES")
else:
    print("NO")