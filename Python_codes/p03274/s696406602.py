n,k = list(map(int, input().split()))
x = list(map(int, input().split()))

# 連続するK地点を選ぶ
cost = 10**18
for i in range(0, n-k+1):
    left = x[i]
    right = x[i+k-1]
    if left < 0 and right < 0:
        cost = min(cost , abs(left))
    elif left > 0 and right > 0:
        cost = min(cost, abs(right))
    else:
        cost = min(cost, min(2 * abs(right) + abs(left), 2 * abs(left) + abs(right)))

print(cost)