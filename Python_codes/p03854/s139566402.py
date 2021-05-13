lt = ["dream", "dreamer", "erase", "eraser"]
s = input()

lt = [w[::-1] for w in lt]
s = s[::-1]
cond = True
i = 0
while i < len(s):
    for t in lt:
        if s[i:].startswith(t):
            i += len(t)
            break
    else:
        cond = False
        break

print("YES" if cond else "NO")
