n=int(input())

n0=n
k=1
for i in range(6):
    if n0<10 :
        break
    n0//=10
    k+=1
if k==1 :
    ans = n%10
else:
    ans = 9
    if k>=3 :
        ans += min(900,n-99)
        if k>=5 :
            ans += min(90000,n-9999)
print(ans)


