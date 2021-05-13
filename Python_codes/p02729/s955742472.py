N, M = map(int, input().split())

def combi(x):
    return x * (x - 1) // 2

print(combi(N) + combi(M))
