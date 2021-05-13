N = int(input())
a = list(map(int, input().split()))
a.sort()
Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += a.pop()
    else:
        Bob += a.pop()
print(Alice - Bob)