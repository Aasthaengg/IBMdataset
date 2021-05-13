s = input()
ans = "Yes"
for i in range(len(s)):
    if i%2!=0 and s[i]=="R":
        ans = "No"
    elif i%2==0 and s[i]=="L":
        ans = "No"
print(ans)
