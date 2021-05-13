N = int(input())
S = [input() for _ in range(N)]

cnt = sum(map(lambda x: x.count('AB'), S))
B_A = len(list(filter(lambda x: x[0] == 'B' and x[-1] == 'A', S)))
B__ = len(list(filter(lambda x: x[0] == 'B' and x[-1] != 'A', S)))
__A = len(list(filter(lambda x: x[0] != 'B' and x[-1] == 'A', S)))

if B_A == 0:
    print(cnt + min(B__, __A))
else:
    if B__ + __A > 0:
        print(cnt + B_A + min(B__, __A))
    else:
        print(cnt + B_A - 1)
