s = input()
cnt = 0
for i in s:
    if i == 'o':
        cnt += 1

print("YES" if cnt + (15 - len(s)) >= 8 else "NO")
