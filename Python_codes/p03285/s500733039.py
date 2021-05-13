N=int(input())
c=4
d=7
ans=0
ans2=0
ans3="No"
for i in range(15):
    ans=d*i
    if ans !=N:
        for j in range(26):
            ans2=ans+c*j
            if ans2==N:
                ans3="Yes"

    else :
        ans3="Yes"

print(ans3)