n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input())-1)
ans=1
if lst[0]==1:
    print(ans)
    exit()
else:
    button=lst[0]
    lst[0]=None

while True:
    p=button
    button=lst[button]
    ans+=1
    if button==1:
        print(ans)
        break
    elif button==None:
        print(-1)
        break
    lst[p]=None