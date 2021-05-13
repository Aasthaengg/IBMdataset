n = int(input())
a = list(map(int, input().split()))

min = 2
max = 2
for i in reversed(a):
    max = max // i * i + i - 1
    min = (min + i - 1) // i * i

if min >= max:
    print("-1")
else:
    print(min, max)
