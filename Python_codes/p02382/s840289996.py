n = int(input())
x = [int(n) for n in input().split()]
y = [int(n) for n in input().split()]
for p in range(1, 4):
    print((sum([abs(a-b)**p for a, b in zip(x, y)])**(1/p)))
print(max([abs(a-b) for a,b in zip(x, y)]))

