import sys
input = sys.stdin.readline

N,M=map(int,input().split())
drinks = []
for _ in range(N):
    a,b = map(int,input().split())
    drinks.append((a,b))

drinks.sort(key=lambda x:x[0])

sum = 0
price = 0
for d in drinks:
    if sum + d[1] < M:
        sum += d[1]
        price += d[0]*d[1]
    else:
        price += d[0]*(M-sum)
        break

print(price)

