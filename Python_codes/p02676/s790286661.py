K = int(input())
S=input()
S1 = list(S)
S2 = len(S1)

if S2 <= K:
    print(S)

else:
    print(S[:K]+'...')