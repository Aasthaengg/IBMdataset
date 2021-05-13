N = int(input())
X_list = list(map(int, input().split()))

X_mean = round(sum(X_list) / N)

physical_sum = sum([(i - X_mean)**2 for i in X_list])
print(physical_sum)