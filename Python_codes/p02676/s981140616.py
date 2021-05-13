K = int(input())
S = input()

i = len(S)

if K >= i:
    print(S)
else:
    print(S[0:K] + "...")