N = int(input())
A_LIST = list(map(int, input().split()))
A_SET = set(A_LIST)
if len(A_SET) == 1:
    if sum(A_SET) == 0:
        print('Yes')
    else:
        print('No')
elif len(A_SET) == 2:
    a1, a2 = sorted(A_SET)
    if a1 == 0 and A_LIST.count(a1) * 3 == N:
        print('Yes')
    else:
        print('No')
elif len(A_SET) == 3:
    a1, a2, a3 = A_SET
    if a1 ^ a2 == a3 and A_LIST.count(a1) ==  A_LIST.count(a2) and A_LIST.count(a2) == A_LIST.count(a3):
        print('Yes')
    else:
        print('No')
else:
    print('No')
