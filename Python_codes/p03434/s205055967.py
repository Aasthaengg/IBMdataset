n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
Alice = 0
Bob = 0

for i in range(len(l)):
    if i % 2 == 0:
        Alice += l[i]
    else:
        Bob += l[i]
print(Alice - Bob)