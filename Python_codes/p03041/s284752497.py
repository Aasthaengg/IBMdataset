N, K = map(int, input().split())
S = input()

if S[K-1] == 'A':
    S = S[:K-1] + 'a' + S[K:]
elif S[K - 1] == 'B':
        S = S[:K - 1] + 'b' + S[K:]
elif S[K-1] == 'C':
    S = S[:K-1] + 'c' + S[K:]
print(S)