A, B, K = [int(s) for s in input().split()]
takahashi = A - K if A - K > 0 else 0
aoki = B - (K - A if takahashi == 0 else 0)
aoki = aoki if aoki > 0 else 0
print(takahashi, aoki)
