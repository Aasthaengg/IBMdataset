s = input()
w = int(input())
ans = ''
for i in range(len(s)):
    ans+=s[i*w]
    if (i+1) * w > len(s) - 1:
        break
print(ans)