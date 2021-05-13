n,a,b=map(int,input().split())


ans=0
if n==1 and a!=b:
    ans=0
elif a==b:
    ans=1
elif a>b:
    ans=0
else:
    s_a = a*(n-1) + b
    s_b = a + b*(n-1)

    ans= s_b - s_a + 1

print(ans)
    

