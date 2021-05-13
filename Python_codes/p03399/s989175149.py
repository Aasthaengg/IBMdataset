s = [int(input()) for i in range(4)]
ans = 0
for i in range(0,3,2):
    if s[i]<s[i+1]:
        ans+=s[i]
    else:
        ans+=s[i+1]
print(ans)
