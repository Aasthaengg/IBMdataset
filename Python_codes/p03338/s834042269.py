n = int(input())
s = input()
ans = 0
for i in range(n-1):
    c = 0
    for j in range(26):
        if chr(j+97) in s[:i+1] and chr(j+97) in s[i+1:]:
            c += 1
    if c > ans:
        ans = c
print(ans)
