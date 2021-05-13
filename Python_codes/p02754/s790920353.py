N, A, B = [int(v) for v in input().rstrip().split()]

ablen = A + B
n = int(N / int(ablen))
num = A * n
m = N % int(ablen)
num += min(m, A)
print(num)
