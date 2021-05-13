n=int(input())
b=list(map(int,input().split()))
ans=[]
while True:
    l=len(b)
    temp=[]
    flag=0
    for i in range(l-1,-1,-1):
        if flag==1 or b[i]!=i+1: temp.append(b[i])
        else:
            ans.append(i+1)
            flag=1
    b=temp[::-1]
    if len(b)==l:
        print(-1)
        exit()
    elif len(b)==0: break
for val in ans[::-1]: print(val)