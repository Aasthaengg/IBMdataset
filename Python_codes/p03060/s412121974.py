n = int(input())
value = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum = 0
for v, c in zip(value, cost):
    if 0 < v - c:
        sum += v - c
print(sum)