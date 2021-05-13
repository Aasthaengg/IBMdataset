x = input()
S = input()

K = int(x)

if K >= len(S):
    print(S)
else:
    print(S[:K] + '...')