A, B, C, K = map(int, input().split())
t = A-B
if abs(A-B) > 10**18:
    print('Unfair')
else:
    print(B-A if K%2 else A-B)