N, A, B = [int(x) for x in input().split()]
ans = max(0, (A + (N - 1) * B) - ((N - 1) * A + B) + 1)
print(ans)