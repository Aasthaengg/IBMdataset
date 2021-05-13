n = int(input())
a = list(map(int, input().split()))
cost = 0

Sum = sum(a) // 2

cand = 0
for i in range(n):
    temp = cand + a[i]
    if abs(cand - Sum) < abs(temp - Sum):break
    cand = temp
cost = abs(Sum - cand) + abs(Sum - (sum(a) - cand))
print(cost)