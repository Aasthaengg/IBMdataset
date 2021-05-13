s = input().split()
k=int(s[0])
s=int(s[1])
ans=0
for i in range(k+1):
    for j in range(k+1):
        if s-i-j <= k and s-i-j>=0:
            ans+=1
print(ans)
