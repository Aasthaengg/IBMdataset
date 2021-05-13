k,s=map(int,input().split())

ans=0
for i in range(k+1):
    for q in range(k+1):
        if i+q+k>=s and i+q<=s:
            ans+=1
print(ans)