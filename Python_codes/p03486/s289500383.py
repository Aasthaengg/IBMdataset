s = list(input())
t = list(input())

s = "".join(sorted(s))
t = "".join(sorted(t)[::-1])

res = "Yes" if s < t else "No"
print(res)

