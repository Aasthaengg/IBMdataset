x=int(input())

def pow(b,x):
    res=b
    while True:
        if res*b<=x:
            res=res*b
        else:
            break
    return res


ans=1
for i in range(2,x+1):
    if i**2<=x:
        ans=max(ans,pow(i,x))
print(ans)