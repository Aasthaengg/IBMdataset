S = list(input())
A = []
for s in S:
    if s in A:
        print('no')
        exit()
    A.append(s)
print('yes')