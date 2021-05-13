def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
ans = 0

for A in range(1, N):
    for B in range(1, N // A + 1):
        if N - A * B < 1:
            break
        ans += 1
    
print(ans)