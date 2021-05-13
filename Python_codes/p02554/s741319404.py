n = int(input())

mod = 10 ** 9 + 7


eight = pow(8, n, mod)
nine = pow(9, n, mod)
ten = pow(10, n, mod)

ans = (ten - nine - nine + eight) % mod


print(ans)