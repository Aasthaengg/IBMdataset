a,b,c=map(int,input().split())
x=sorted([a,b,c])
count=0
if sum(x)%2==x[2]%2:
    while True:
        if x[1]==x[2] and x[0]==x[2]:
            break
        elif x[1]==x[2] and x[0]!=x[2]:
            x[0]+=2
        else:
            x[1]+=1
            x[0]+=1
        count+=1

else:
    x[2]+=1
    x[0]+=1
    count+=1
    while True:
        if x[1]==x[2] and x[0]==x[2]:
                break
        elif x[1]==x[2] and x[0]!=x[2]:
            x[0]+=2
        else:
            x[1]+=1
            x[0]+=1
        count+=1
print(count)