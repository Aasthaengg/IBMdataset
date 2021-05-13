N = int(input())
A = list(map(int, input().split()))

a = 1
for i in A:
    a *= i
b = 0
for j in A:
    b += a / j

print(a/b)