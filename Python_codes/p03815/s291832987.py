n=int(input())
n-=1
ans=(n//11)*2
if n%11<=5:
    ans+=1
else:
    ans+=2
print(ans)