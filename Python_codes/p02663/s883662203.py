h1,m1,h2,m2,k=map(int,input().split())
hm1=60*h1+m1
hm2=60*h2+m2
ans=hm2-hm1-k
print(ans)