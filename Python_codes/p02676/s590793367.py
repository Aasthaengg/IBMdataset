K = int(input())
S = input()

S_num = len(S)

if K >= S_num:
    print(S)
else:
    print(S[:K] + "...") 