[n,m]=list(map(int,input().split()))
if m-2*n>=0:
    ans=n+(m-2*n)//4
else:
    ans=m//2
print(ans)
