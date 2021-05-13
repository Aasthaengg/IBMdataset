from scipy.special import comb
# a = comb(n, r)
n,k=map(int,input().split())
p=n//k
q=p+1
ans=0
ans1 = (comb(p, 3, exact=True)+comb(p, 2, exact=True))*6+p
ans2 = (comb(q, 3, exact=True)+comb(q, 2, exact=True))*6+q
ans+=ans1
if k%2==0:
    if k*p+k//2>n:
        ans+=ans1
    else:
        ans+=ans2
# print(p)
# print(q)
print(ans)