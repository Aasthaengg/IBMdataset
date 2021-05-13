A, B, C = map(int, input().split())
if B >= C:
    ans = B + C
elif C <= A + B:
    ans = B + C
else:
    ans = 2 * B + A + 1

print(ans)