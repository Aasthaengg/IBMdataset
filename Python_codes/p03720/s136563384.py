def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, M = MI()
city = [[] for _ in range(N)]

for _ in range(M):
    a, b = MI()
    city[a - 1].append(b - 1)
    city[b - 1].append(a - 1)
    
for c in city:
    print(len(c))