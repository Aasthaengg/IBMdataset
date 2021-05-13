K = int(input())
S = input()
s_l = len(S)

if K >= s_l:print(S)
else:print(S[:K]+'...')