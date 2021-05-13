S = input()

ans = 0
for i, s in enumerate(S):
    hand = "p" if i & 1 else "g"
    if s == "g" and hand == "p":
        ans += 1
    elif s == "p" and hand == "g":
        ans -= 1
    else:
        continue

print(ans)
