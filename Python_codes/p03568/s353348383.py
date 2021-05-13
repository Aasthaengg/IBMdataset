n = int(input())
a = list(map(int, input().split()))

total = 3 ** n
odd = 1

for i in range(n):
    if a[i] % 2 == 0:
        odd *= 2
    else:
        odd *= 1

print(total - odd)