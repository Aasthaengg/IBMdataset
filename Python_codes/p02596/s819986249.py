k = int(input())
remainder = [0] * k
remainder[0] = 7 % k
if remainder[0] == 0:
    print(1)
    exit()
for i in range(1, k):
    remainder[i] = (10 * remainder[i - 1] + 7) % k
    if remainder[i] == 0:
        print(i + 1)
        exit()
print('-1')