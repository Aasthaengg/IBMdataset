N = int(input())
S = input()
black = 0
ans = 0

for s in S:
    if s == "#":
        black += 1
    else:
        if black > 0:
            ans += 1
            black -= 1

print(ans)