n = int(input())
a = list(map(int, input().split()))

eo = [i % 2 == 0 for i in a]

even = eo.count(True)
odd = n - even

ans = 3 ** n - 2 ** even
print(ans)
