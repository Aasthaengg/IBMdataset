n, m, d = map(int, input().split())

answer = (n - d) * (m - 1) / (n ** 2)
if d != 0:
    answer *= 2
print(answer)
