N = int(input())
A = list(map(int, input().split()))
neg_parity = sum(a < 0 for a in A) % 2
A = sorted(a if a >= 0 else -a for a in A)
print(sum(A) - neg_parity * 2 * A[0])