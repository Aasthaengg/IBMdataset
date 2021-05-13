N = int(input())
A = list(map(int, input().split()))
neg_cnt = sum(a < 0 for a in A)
A = sorted(a if a >= 0 else -a for a in A)
if neg_cnt % 2:
    print(sum(A) - 2 * A[0])
else:
    print(sum(A))
