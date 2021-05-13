s = list(input())
t = input()
ans = "No"

for _ in range(len(s)):
    if "".join(s) == t:
        ans = "Yes"
        break
    else:
        last_s = s.pop(-1)
        s.insert(0, last_s)
print(ans)
