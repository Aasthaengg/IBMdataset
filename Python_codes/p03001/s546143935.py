a, b, x, y = map(int, input().split())
ab= a*b
ans1 = ab/2
ans2 = 0


if b/2 == y and a/2 == x:
    ans2 = 1
print(ans1, ans2)