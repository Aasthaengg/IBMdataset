I=lambda:list(map(int,input().split()))
I()
F=lambda x:sum(j*(len(x)-1-2*i)for i,j in enumerate(x))
print(F(I())*F(I())%(10**9+7))