s = input()
ans = 0
cnt = 0
left = 200005
right = 0
for i in range(len(s)):
    if (s[i]=='A') : 
        left = min(left, i)
    if (s[i]  == "Z") :
        right = max(right, i)
print(right - left+1)