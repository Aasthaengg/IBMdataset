a, b, c, d = [int(input()) for i in range(4)]
fare_for_train = min(a, b)
fare_for_bus = min(c, d)
ans = fare_for_train + fare_for_bus
print(ans)