s = list(input())

odd = s[::2]
even = s[1::2]
ans = "Yes"

if "L" in odd or "R" in even:
    ans = "No"

print(ans)