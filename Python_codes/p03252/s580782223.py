S = input()
T = input()
D = dict()

for s, t in zip(S, T):
    if s in D:
        if D[s] != t:
            print('No')
            exit()
    elif t in D.values():
        print('No')
        exit()
    else:
        D[s] = t

print('Yes')