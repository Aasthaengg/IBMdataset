n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
temp = list(map(lambda x, y: abs(x-y), X, Y))
result = []
for i in [1,2,3]:
    print(sum(list(map(lambda x: x**i, temp)))**(1/i))
print(max(temp))
