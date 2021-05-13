N, K, Q = list(map(int, input().split()))

scores = [K-Q] * N
for i in range(Q):
    scores[int(input()) - 1] += 1

for score in scores:
    if score > 0:
        print('Yes')
    else:
        print('No')