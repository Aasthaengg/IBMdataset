S = input()
S_set = list(set(S))

if len(S) == len(S_set):
    print("yes")
else:
    print("no")
