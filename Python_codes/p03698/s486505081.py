s = input()
t = {s[i] for i in range(len(s))}

ans = "yes" if len(s) == len(t) else "no"
print(ans)
