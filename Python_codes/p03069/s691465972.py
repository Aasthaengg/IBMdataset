n = int(input())
s = list(map(str,input()))
left = 0
right = 0
for i in range(n):
    if s[i]==".":
        right += 1
ans = right
if s[0]==".":
    right -= 1
for j in range(1,n):
    if s[j-1]=="#":
        left += 1
    if s[j]==".":
        right -= 1
    ans = min([ans,left+right])
if s[n-1]=="#":
    left += 1
ans = min([ans,left])
print(ans)
