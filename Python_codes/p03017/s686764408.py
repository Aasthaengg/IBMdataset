import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

N,A,B,C,D = map(int,input().split())
S = input()
A -= 1; B -= 1; C -= 1; D -= 1

def find_route(X,Y):
    for i in range(X,Y):
        if S[i] == S[i + 1] == '#':
            return False
    return True

if C < D:
    if find_route(A,C) and find_route(B,D):
        print('Yes')
    else:
        print('No')
else:
    flag = False
    for i in range(B - 1,D):
        if S[i] == S[i + 1] == S[i + 2] == '.':
            flag = True
            break
    if flag and find_route(A,C):
        print('Yes')
    else:
        print('No')


