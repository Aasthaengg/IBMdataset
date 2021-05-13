n = int(input())
s = input()
ans=0
for stone in s:
    if stone==".":
        ans+=1
ans_mn=ans
for i in range(len(s)):
    if s[i]=="#":
        ans+=1
    if s[i]==".":
        ans-=1
    if ans < ans_mn:
        ans_mn=ans
print(ans_mn)