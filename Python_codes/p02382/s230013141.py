n = int(input())
x = map(float, input().strip().split())
y = map(float, input().strip().split())
d = tuple(map(lambda x,y:abs(x-y), x, y))
print(sum(d))
print(sum(map(pow, d, [2]*n))**0.5)
print(sum(map(pow, d, [3]*n))**(1/3))
print(max(d))