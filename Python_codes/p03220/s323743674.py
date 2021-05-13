def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
T, A = MI()
H = list(map(lambda x : T - 0.006 * int(x), input().split()))

for i in range(N):
    H[i] = abs(H[i] - A)
    
ans = H.index(min(H)) + 1

print(ans)