def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, K = MI()
S = input()
T = S.lower()
S = list(S)
T = list(T)

S[K - 1] = T[K - 1]

print("".join(map(str, S)))