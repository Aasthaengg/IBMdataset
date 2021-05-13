s = input()
h = input()
cnt = 0
for i in range(len(s)):
    if s[i] != h[i]:
        cnt = cnt+1

print(cnt)