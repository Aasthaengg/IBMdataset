s = input()[::-1]
templates = [s[::-1] for s in ["dream", "dreamer", "erase", "eraser"]]
while s:
    for template in templates:
        if s.startswith(template):
            s = s.replace(template, "", 1)
            break
    else:
        break
print("YES" if not s else "NO")