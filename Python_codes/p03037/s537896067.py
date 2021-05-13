def INT():
    return int(input())

def LI():
    return list(map(int, input().split()))

def MI():
    return map(int, input().split())

N, M = MI()
gate = [0] * (N + 2)
ans = 0

for _ in range(M):
    L, R = MI()
    gate[L] += 1
    gate[R + 1] -= 1

for i in range(1, N + 1):
    gate[i] += gate[i - 1]
    
for i in range(1, N + 1):
    if gate[i] == M:
        ans += 1
        
print(ans)