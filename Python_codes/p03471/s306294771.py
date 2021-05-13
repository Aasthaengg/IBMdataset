n,y=map(int,input().split())
count=0
for a in range(n+1):
    for b in range(n+1-a):
            if 10000*a+5000*b+1000*(n-b-a)==y:
                print(a,b,n-a-b)
                count=count+1
                break
    else:
        continue
    break
if count==0:
    print(-1,-1,-1)
else:
    pass