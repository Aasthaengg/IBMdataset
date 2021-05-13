n = int(input())
ss = input()
ans = 0
total = 0
for s in ss:
    if s == "I":
        total += 1
        ans = max(ans, total)
    else:
        total -= 1
print(ans)