s = input()
s = s.replace("BC", "X")

ans = 0
a_count = 0

for i in range(len(s)):
    if s[i] == "A":
        a_count += 1
    elif s[i] == "X":
        ans += a_count
    else:
        a_count = 0

print(ans)