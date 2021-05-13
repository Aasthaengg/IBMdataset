l = sorted(list(map(int, input().split())))
A, B, C = map(int, l)

ans = 0

while C - A >= 2:
    A += 2
    ans += 1

while C - B >= 2:
    B += 2
    ans += 1


if A == B == C:
    print(ans)
elif C - A == 1 and C - B == 1:
    ans += 1
    print(ans)
else:
    ans += 2
    print(ans)
