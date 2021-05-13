def solve(s):
    t = "AKIHABARA"
    u = ""
    i, j = 0, 0
    if len(s) > len(t):
        return "NO"
    while True:
        if len(t) <= i:
            break
        if (j < len(s)) and (t[i] == s[j]):
            u += s[j]
            i += 1
            j += 1
        elif t[i] == "A":
            u += "A"
            i += 1
        else:
            break
    return "YES" if (u == t) else "NO"

assert solve("KIHBR") == "YES"
assert solve("AKIBAHARA") == "NO"
assert solve("AAKIAHBAARA") == "NO"

s = input()
print(solve(s))