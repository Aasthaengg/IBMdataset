n = int(input())
a = [int(s) for s in input().split()]

m = 0
for num in a:
    if num % 2 == 0:
        m += 1
print(3 ** n - 2 ** m)