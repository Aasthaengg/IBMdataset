n,m=map(int,input().split())
list1=[]
listn=[]
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        list1.append(b)
    elif b==1:
        list1.append(a)
    elif a==n:
        listn.append(b)
    elif b==n:
        listn.append(a)
list1=set(list1)
listn=set(listn)
ans=0
if len(listn)!=0:
    for i in range(len(list1)):
        num=list1.pop()
        if num in listn:
            ans=1
            break
if ans==1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
