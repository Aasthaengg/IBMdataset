n=int(input())
tmp=0
for i in range(1,10000000):
    tmp+=i
    if tmp>n:
        a=i-1
        tmp-=i
        break
    elif tmp==n:
        for j in range(i):
            print(j+1)
        exit()
x=n-tmp#ずらす個数
y=a-x#ずらさない個数
#print(a,tmp,x,y)
ans=[]
for i in range(1,a+1):
    if i<=y:
        ans.append(i)
    else:
        ans.append(i+1)
#print(ans)
[print(i) for i in ans]