n, k, q = map(int, input().split())
A = [k - q] * n
for _ in range(q):
    A[int(input())-1] += 1
for a in A:
    print('Yes') if a > 0 else print('No')