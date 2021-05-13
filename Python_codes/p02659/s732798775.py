a,b=input().split()
a=int(a)
b=b.replace(".","")
b=int(b)
ans=str(a*b)
if (len(ans)>=3):
    print(ans[:-2])
else:
    print(0)
