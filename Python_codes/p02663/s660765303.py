h1,m1,h2,m2,k=map(int, input().split())

ans=0
if m1>m2: ans=(h2-h1-1)*60+60-m1+m2
else: ans=(h2-h1)*60+m2-m1
print(ans-k)
