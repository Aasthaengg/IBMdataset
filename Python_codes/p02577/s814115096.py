import math

n = input()

n_list = map(int, list(n))
ans = sum(n_list)

print("Yes" if (ans % 9) == 0 else "No")
