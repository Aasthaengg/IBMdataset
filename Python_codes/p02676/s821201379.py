K = int(input())
S = input()

if len(S) <= K:
    print(S)
else:
    str = ''
    for i in range(K):
        str += S[i]
    str += "..."
    print(str)
