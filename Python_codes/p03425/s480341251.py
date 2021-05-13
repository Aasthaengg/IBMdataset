# だるいので強引

n = int(input())
d = {}
dd = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(n):
    s = input()
    if s[0] in list("MARCH") and s not in d:
        d[s] = True
        dd[s[0]] += 1

ans = 0
ans += dd["M"] * dd["A"] * dd["R"]
ans += dd["M"] * dd["A"] * dd["C"]
ans += dd["M"] * dd["A"] * dd["H"]
ans += dd["M"] * dd["R"] * dd["C"]
ans += dd["M"] * dd["R"] * dd["H"]
ans += dd["M"] * dd["C"] * dd["H"]
ans += dd["A"] * dd["R"] * dd["C"]
ans += dd["A"] * dd["R"] * dd["H"]
ans += dd["A"] * dd["C"] * dd["H"]
ans += dd["R"] * dd["C"] * dd["H"]
print(ans)
