n=int(input())
s=list(input())
ans=0
for i in range(1,n):
    if s[i] == "E":
        ans += 1
        
ans_=ans
for i in range(1,n):
    if s[i-1] == "W":
        ans_+= 1
    if s[i] == "E":
        ans_+= -1
    ans = min(ans,ans_)
print(ans)