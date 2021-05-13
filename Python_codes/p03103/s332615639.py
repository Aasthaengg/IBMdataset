n,m = map(int,input().split())
energy = []
for i in range(n):
    a,b = map(int,input().split())
    energy.append([a,b])

energy.sort(key=lambda x:x[0])

money = 0

for i in range(n):
    if energy[i][1] < m:
        m -= energy[i][1]
        money += energy[i][1] * energy[i][0]
    else:
        money += energy[i][0] * m
        break
print(money)