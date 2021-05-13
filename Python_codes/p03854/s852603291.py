s = input()
s = s[::-1]
t = ["dream", "dreamer", "erase", "eraser"]
for i in range(len(t)):
    t[i] = t[i][::-1]
can = True
i = 0
while i < len(s):
    can2 = False
    for j in range(len(t)):
        d = t[j]
        if s[i:i+len(d)] == d:
            can2 = True
            i += len(d)
    if not can2:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")