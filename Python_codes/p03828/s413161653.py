n = int(input())
num = [0]*(n+1)
ans = 1
for i in range(2,n+1):
    j=2
    while j<n+1 and i>1:
        if i%j==0:
            i=i//j
            num[j]+=1
        else:
            j+=1
for i in num:
    ans=ans*(i+1)%1000000007
print(ans)
