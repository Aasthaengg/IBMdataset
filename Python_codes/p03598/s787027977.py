n = int(input())
k = int(input())
x = list(map(int, input().split()))
sum_distance = 0
for i in range(len(x)):
    sum_distance += min(x[i], k - x[i]) * 2
print(sum_distance)
