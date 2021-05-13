n = int(input())
a = list(map(int,input().split()))

currentmoney = 1000
stock = 0

for i in range(n-1):
    if a[i] <= a[i+1]:
        stock += currentmoney // a[i]
        currentmoney -= a[i] * (currentmoney // a[i])
        currentmoney += stock * a[i+1]
        stock = 0

print(currentmoney)