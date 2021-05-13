w,a,b=map(int,input().split())

if a<=b:
    ans=b-(w+a)
else:
    ans=a-(w+b)

if ans>0:
    print(ans)
else:
    print("0")