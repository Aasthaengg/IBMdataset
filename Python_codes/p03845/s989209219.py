def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
T = LI()
M = INT()

ans = sum(T)

for i in range(M):
    tmp = ans
    P, X = MI()
    tmp = tmp - T[P - 1] + X
    print(tmp)