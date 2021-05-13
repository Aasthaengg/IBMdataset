n=int(input())
a,b=[list(map(int,input().split())) for i in range(2)]
if sum(a) >sum(b):print("No")
elif sum(a)==sum(b):

    for x,c in zip(a,b):
        if x!=c:print("No");exit()
    print("Yes")
else:
    cnt=sum(b)-sum(a)
    v=cnt
    for x,y in zip(a,b):
        if x>=y:v-=(x-y)
        else:
            v-=(x+y)%2
            cnt-=(y-x+(x+y)%2)//2
    print("Yes") if cnt*2==v and cnt>=0 and v>=0 else print("No")