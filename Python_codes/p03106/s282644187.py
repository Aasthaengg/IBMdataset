a, b, k = map(int, input().split())
CD = []
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        CD.append(i)
print(CD[k - 1])