k,s=map(int,input().split())
count=0
for x in range(k+1):
    w=s-x
    if w>=0:
        for y in range(k+1):
            v=w-y
            if k>=v>=0:
                count=count+1
            else:
                pass
    else:
        pass
print(count)