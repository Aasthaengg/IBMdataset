n = int(input())
a = sorted(map(int, input().split()), reverse=True)
Alice = 0
Bob = 0
for i in range(n):
    if i % 2 == 0:
        Alice += a[i]
    else:
        Bob += a[i]
print(Alice - Bob)
