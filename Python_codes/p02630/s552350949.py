from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
sum_res = sum(A)
counter = Counter(A)

for _ in range(Q):
    B, C = map(int, input().split())
    sum_res += (C - B) * counter[B]
    counter[C] += counter[B]
    counter[B] = 0
    print(sum_res)
