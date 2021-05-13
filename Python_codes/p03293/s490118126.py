S = input()
T = input()

rolled = S

ans = "No"

for _ in S:
    rolled = rolled[-1] + rolled[:-1]
    if rolled == T:
        ans = "Yes"
        break

print(ans)