s = input()
S = 0

ans = len(s)
for i in s:
    if i == "S":
        S += 1
    else:
        if S > 0:
            ans -= 2
            S -= 1
print(ans)