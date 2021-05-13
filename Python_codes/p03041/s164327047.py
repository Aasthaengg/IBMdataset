N, K = [int(_) for _ in input().split()]
S = list(input())

S[K-1] = S[K-1].lower()
print("".join(S))
