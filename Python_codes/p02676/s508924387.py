K = int(input())
S = list(input())

if len(S) <= K:
    print("".join(S))
else:
    tmp = [S[i] for i in range(K)]
    print("".join(tmp) + "...")
