n, k, q = map(int, input().split())
n_score = [0] * n
for i in range(q):
    n_score[int(input()) - 1] += 1

for j in n_score:
    if k + j - q > 0:
        print('Yes')
    else:
        print('No')