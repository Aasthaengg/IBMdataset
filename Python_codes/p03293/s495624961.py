S = list(input())
T = list(input())
flag = True
for _ in range(len(S)):
    last = S.pop()
    S.insert(0, last)
    if S == T:
        print('Yes')
        flag = False
        break
if flag:
    print('No')