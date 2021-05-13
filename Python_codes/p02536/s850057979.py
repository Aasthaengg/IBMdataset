import sys
sys.setrecursionlimit(1000000)

def find(Data, x):
    if Data[x] < 0:
        return x
    else:
        Data[x] = find(Data, Data[x])
        return Data[x] 

def unite(Data, a, b):
    a, b = find(Data, a), find(Data, b)
    if a == b:
        pass
    elif Data[a] < Data[b]:
        Data[a] = Data[a] + Data[b]
        Data[b] = a
    else:
        Data[b] = Data[b] + Data[a]
        Data[a] = b 

n, m = map(int, input().split())
UF = [-1 for i in range(n)]
for i in range(m):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    unite(UF, ai, bi)

ans = 0
for i in range(n):
    if UF[i] < 0: ans += 1 
print(ans - 1)