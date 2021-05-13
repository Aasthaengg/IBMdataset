n=int(input())
s=list(input())
ans=0
for i in range(1,n+1):
    left_set=set(s[:i])
    right_set=set(s[i:])
    ans=max(ans,(len(left_set & right_set)))

print(ans)