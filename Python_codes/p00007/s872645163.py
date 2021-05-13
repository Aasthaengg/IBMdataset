a=int(input())
b=100000
for i in range(a):
    ans=b*1.05
    if ans%1000!=0 :
        ans=ans+(1000-ans%1000)
        b=ans
    else:
        b=ans
print(int(b))