n = int(input())
array = list(map(int,input().split()))
a = b = 0
for i, m in enumerate(sorted(array, reverse=True)):
    if i == 0 or i % 2 == 0:
        a += m
    if i % 2 != 0:
        b += m
print(a-b)