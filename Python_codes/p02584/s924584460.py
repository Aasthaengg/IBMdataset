x,k,d=map(int,input().split())
if x<0:
    x*=(-1)
z=x//d
ans_p=x-z*d
ans_n=-(ans_p-d)
if k<z:
    ans=x-k*d
elif k==z:
    ans=ans_p
else:
    num=k-z
    if num%2==1:
        ans=ans_n
    else:
        ans=ans_p
print(ans)