A, B, C = [int(x) for x in input().split()]
if C > A + B:
    ans = A + 2 * B + 1
else:
    ans = B + C
print(ans)