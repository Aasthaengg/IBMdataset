n = int(input())
a = list(map(int, input().split()))

is_ball_contains = [0] * (n+1)
for i in range(n, 0, -1):
    if sum(is_ball_contains[i::i]) % 2 != a[i-1]:
        is_ball_contains[i] = 1

print(sum(is_ball_contains))
print(' '.join([str(i) for i, v in enumerate(is_ball_contains) if v]))
