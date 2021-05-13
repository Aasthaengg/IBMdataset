N, K = map(int, input().split())
S = input()

print(S[:K-1], end='')

if K == N:
    print(S[K-1].lower())
else:
    print(S[K-1].lower(), end='')
    print(S[K:])