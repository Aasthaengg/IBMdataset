from operator import mul
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
count = 0

for i in range(n):
    a = list(map(int, input().split()))
    com = map(mul, a, b)
    if sum(com) + c > 0:
        count += 1
    a.clear()

print(count)