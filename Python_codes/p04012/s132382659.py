W = input()

ok = [True] * 26

for w in W:
    idx = ord(w) - ord("a")
    ok[idx] = not ok[idx]

print("Yes" if all(ok) else "No")