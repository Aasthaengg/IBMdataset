# AGC030
A, B, C = map(int, input().split())
if A + B >= C:
    ans = B + C
else:
    if B >= C:
        ans = B + C
    else:
        ans = 2 * B + A + 1
print(ans)