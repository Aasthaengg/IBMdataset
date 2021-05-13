def ans(s,t):
    for i in range(len(s)):
        s = s[-1] + s[:-1]

        if s == t:
            return "Yes"
    return "No"

s = input()
t = input()

ans = ans(s,t)

print(ans)