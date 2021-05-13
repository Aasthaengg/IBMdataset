N = int(input())
A = list(map(int, input().split()))

res = True

for num in A:
    if num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
        res = False
        break

print(['DENIED', 'APPROVED'][res])