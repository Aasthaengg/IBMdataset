s = input()

s_odd = []
for i in range(0, len(s)):
    if i % 2 == 0:
        s_odd.append(s[i])

print("".join(s_odd))
