n=int(input())
ans=""
k=0
while n!=0:
    ans=str(n%2)+ans
    n=n-(n%2)*(-1)**k
    n=n//2
    k+=1
if ans=="":
    ans=0
print(ans)
