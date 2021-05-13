s = input()
s = s[::-1]
ans = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue 
    else:
        ans += 1
print(ans)