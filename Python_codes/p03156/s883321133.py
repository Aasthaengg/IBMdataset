n=int(input())
a,b=map(int, input().split())
*p,=map(int, input().split())
mn,md,mx=0,0,0
for pi in p:
    if pi<=a:
        mn+=1
    elif pi<=b:
        md+=1
    else:
        mx+=1
print(min(mn,md,mx))
