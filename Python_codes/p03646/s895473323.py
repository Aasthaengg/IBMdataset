K = int(input())
N = 50
a = [i for i in range(50)]
d, m = divmod(K, N)
for i in range(N):
  a[i] += d
  if N - i <= m:
    a[i] += 1

print(N)
print(" ".join(map(str, a))) 