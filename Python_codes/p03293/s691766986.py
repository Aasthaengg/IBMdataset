S = list(input())
T = list(input())
for i in range(len(S)):
    T.insert(0, T.pop(-1))
    if S == T:
        print('Yes')
        break
else:
    print('No')