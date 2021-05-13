n = int(input())
mod = 10 ** 9 + 7
ten = 10 ** n % mod
nine = 9 ** n % mod
eight = 8 ** n % mod

ans = (ten - nine - nine + eight) % mod
print(ans)