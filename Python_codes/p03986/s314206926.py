X=input()
ans=len(X)
count_s=0
for i in X:
    if i=='S':
        count_s+=1
    if i=='T' and count_s>=1:
        count_s-=1
        ans-=2

print(ans)