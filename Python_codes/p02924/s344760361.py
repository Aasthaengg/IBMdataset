# 1-nまでの k の和
def sigma1(n):
    return n * (n + 1) // 2
n = int(input())
print(sigma1(n-1))