s = input()
templates = ["dream", "dreamer", "erase", "eraser"]
while s:
    for template in templates:
        if s.endswith(template):
            s = s[:-len(template)]
            break
    else:
        break
print("YES" if not s else "NO")