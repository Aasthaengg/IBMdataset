a, b, k = map(int, input().split())

c = [1]
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        k -= 1
        if k == 0:
            print(i)