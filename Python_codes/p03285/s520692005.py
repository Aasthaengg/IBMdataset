n = int(input())
ans = "No"
for f in range(26):
    for s in range(15):
        if f * 4 + s * 7 == n:
            ans = "Yes"
            break

print(ans)
