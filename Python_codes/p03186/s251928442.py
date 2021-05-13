a,b,c=map(int,input().split(" "))
if c>a+b:
    ans=a+b*2+1
else:
    ans=b+c
print(ans)