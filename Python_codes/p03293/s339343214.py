s = input()
t = input()
ans = 'No'
if t==s:
    ans = "Yes"
for i in range(len(s)):
    s = "".join([s[-1],s[:len(s)-1]])
    if t==s:
        ans = "Yes"
print(ans)