# -*- coding: utf-8 -*-
N, A, B = map(int, input().split(' '))
X = list(map(int, input().split(' ')))

diffs = [X[i+1] - X[i] for i in range(N-1)]
ans = 0
for diff in diffs:
    # print(A * diff, B)
    ans += min(A*diff, B)

print (ans)