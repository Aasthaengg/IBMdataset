K = int(input())
S = input()

if K - len(S) >= 0:
    print(S)
else:
    print("{}...".format(S[0:K]))