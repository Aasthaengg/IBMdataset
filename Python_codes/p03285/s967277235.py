N = int(input())
ans = "No"
for x in range(26):
    for y in range(15):
        if x * 4 + y * 7 == N:
            ans = "Yes"
            break

print(ans)
