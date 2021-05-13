A, B, C = map(int, raw_input().split())

if A+B >= C:
    ans = B+C
elif A+B < C:
    ans = 2*B + A + 1

print ans