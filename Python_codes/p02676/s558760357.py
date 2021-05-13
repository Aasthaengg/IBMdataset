K = int(input())
S = input()
S_length = len(S)
if K >= S_length:
    print(S)
else:
    tmp = S[:K] + '...'
    print(tmp)
