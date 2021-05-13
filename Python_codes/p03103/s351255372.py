n,m = map(int,input().split())

lis = []

for _ in range(n):
    a,b = map(int, input().split())
    lis.append([a,b])
    
lis = sorted(lis)

total = 0
cash = 0

for i in range(n):
    if total < m:
        total += lis[i][1]
        cash += lis[i][0] * lis[i][1]
        if total >= m:
            total -= lis[i][1]
            cash -= lis[i][0] * lis[i][1]
            for j in range(lis[i][1]):
                while total < m:
                    total += 1
                    cash += lis[i][0]
    else:
        break

print(cash)