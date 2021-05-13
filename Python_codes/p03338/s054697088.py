n=int(input())
s=input()
left=set()
ans=0

for i in range(n-1):
    left.add(s[i])
    right=set()
    for j in range(i+1,n):
        right.add(s[j])
    cnt=0
    for ll in left:
        if ll in right:
            cnt+=1
    ans=max(ans,cnt)

print(ans)