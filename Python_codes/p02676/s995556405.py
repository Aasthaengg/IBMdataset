K = int(input())
S = input()

if K < len(S):
    print(S[0:K] + "...")

else:
    print(S)