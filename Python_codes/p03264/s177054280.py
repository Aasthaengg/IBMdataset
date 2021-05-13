# ABC108A

k = int(input())
odd = k // 2
if k % 2 == 1:
    odd += 1
print(odd * (k-odd))
