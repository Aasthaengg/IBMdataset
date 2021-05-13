N, *P = map(int, open(0).read().split())
pairs = sorted((P[i], i) for i in range(N))

sub = 1
right = 0
for left in range(N):
    while right < N - 1 and pairs[right + 1][1] > pairs[right][1]:
        right += 1

    sub = max(sub, right - left + 1)

    if left == right:
        right += 1
print(N - sub)
