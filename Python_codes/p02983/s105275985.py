l,r=map(int,input().split())
ans=l*r
if l//2019!=r//2019:
    ans=0
elif l%2019==0 or r%2019==0:
    ans=0
else:
    num1=l%2019
    num2=r%2019
    for i in range(num1,num2):
        for j in range(i+1,num2+1):
            num=(i*j)%2019
            if ans>num:
                ans=num
print(ans)
