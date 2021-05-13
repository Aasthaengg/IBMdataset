N, K = (int(x) for x in input().split())
S = input()

S = S[:K-1] +S[K-1].lower() +S[K:]
print(S)
