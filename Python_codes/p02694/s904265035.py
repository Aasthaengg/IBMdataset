X = int(input())
M = 100
ans = 0

while X > M:
    tax = M // 100
    M += tax
    ans += 1

print(ans)