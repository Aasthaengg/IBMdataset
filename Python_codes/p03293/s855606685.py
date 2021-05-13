S=list(input())
T=list(input())

for _ in range(len(S)):
    c = S.pop(0)
    S.append(c)
    if S == T:
        print('Yes')
        exit()

print('No')