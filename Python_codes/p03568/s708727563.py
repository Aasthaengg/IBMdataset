N = int(input())
A = list(map(int, input().split()))
x = 1
y = 1
for a in A:
    x *= 3
    if a%2 == 0:
        y *= 2
print(x-y)