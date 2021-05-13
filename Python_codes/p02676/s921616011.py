K = int(input())
S = input()
result = ''
if len(S) <= K:
    print(S)
    exit()
elif len(S) > K:
    for i in range(K):
        result += S[i]
    result += '...'
    print(result)
    exit()