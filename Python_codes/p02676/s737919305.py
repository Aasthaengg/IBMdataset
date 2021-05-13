K = int(input())
S = input(str())

if K >= len(S):
    print(S)
else:
    print(S[:+ K], ("..."), sep='')