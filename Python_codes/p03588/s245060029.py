n = int(input())
ma = 0
value = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > ma:
        ma = a
        value = b

print(ma + value)