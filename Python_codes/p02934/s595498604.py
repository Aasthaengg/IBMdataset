N = int(input())
A = list(map(int, input().split()))
x = 0
for ai in A:
    x += 1 / ai
print(1 / x)
