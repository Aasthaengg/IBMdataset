N = int(input())
ryukasu = [2, 1]
for i in range(2, 87):
    ryukasu.append(ryukasu[i-2] + ryukasu[i-1])
print(ryukasu[N])