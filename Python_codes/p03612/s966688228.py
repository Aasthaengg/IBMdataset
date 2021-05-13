N = int(input())
P_s = list(map(int, input().split()))

orders = [i + 1 for i in range(N)]
total = 0

for i in range(N - 1):
    p = P_s[i]
    n = orders[i]
    
    if (n == p):
        tmp = P_s[i]
        P_s[i] = P_s[i + 1]
        P_s[i + 1] = tmp
        
        total += 1

if (P_s[N - 1] == N):
    total += 1

print(total)
