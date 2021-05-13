n = int(input())
seq = 1
for i in range(1, n + 1):
    seq *= i
    seq %= 1e9 + 7
print(int(seq))