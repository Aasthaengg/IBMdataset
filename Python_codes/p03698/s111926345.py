S = input()

lis_S = list(S)
set_S = set(S)

if len(lis_S) == len(set_S):
    print("yes")
else:
    print("no")