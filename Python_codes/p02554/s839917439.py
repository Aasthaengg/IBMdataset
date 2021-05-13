n = int(input())
a1 = 9 ** n
a2 = 9 ** n
a3 = 8 ** n
ans = 10**n - (a1 + a2 - a3)
print(ans%(10**9+7))