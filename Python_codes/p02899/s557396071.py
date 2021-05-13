n = int(input())
A = tuple(map(int, input().split()))
A = [(idx+1, a) for idx, a in enumerate(A)]
A = sorted(A, key=lambda x: x[1])
print(*[idx for idx, a in A])
