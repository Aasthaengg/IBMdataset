a,b,c= list(map(int, input().split()))
i=0

for i in range(0,10):
    ans=a*c-b
    print(ans)
    c=ans
