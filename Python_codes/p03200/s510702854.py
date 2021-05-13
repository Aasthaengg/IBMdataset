S = input()
ans = 0
black = 0
for c in S:
    if c == "B":
        black += 1
    else:
        ans += black
print(ans)