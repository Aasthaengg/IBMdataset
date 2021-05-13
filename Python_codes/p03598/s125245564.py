n = int(input())
k = int(input())
x = list(map(int, input().split()))

distance = 0

for i in range(len(x)):
    if x[i] < k - x[i]:
        distance += x[i] * 2
    else:
        distance += (k - x[i]) * 2

print(distance)