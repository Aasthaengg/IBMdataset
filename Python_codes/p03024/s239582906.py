s=list(input())
cnt=0
for i in range(len(s)):
    if s[i]=="x":
        cnt+=1
if cnt > 7:
    print("NO")
else:
    print("YES")
