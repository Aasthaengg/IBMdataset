N, *AB = [int(x) for x in input().split()]
A, B = sorted(AB)
if (B - A) % 2 == 0:
    ans = (B - A) // 2
else:
    ans = (B - A + 2 * min(N - B, A - 1) + 1) // 2
print(ans)