a,b,c=map(int,input().split());ans=0
for i in range(a,b+1):ans+=(c%i==0)
print(ans)
