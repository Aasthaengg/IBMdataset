l=[int(input()) for _ in range(6)]
m=min(l[1:6])
if l[0]%m==0: ans=l[0]//m
else: ans=l[0]//m+1
print(ans+4)