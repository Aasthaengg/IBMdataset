k = int(input())
a = [49 for _ in range(50)]
for i in range(50):
  a[i] += k // 50
for i in range(k % 50):
  a[i] += 51
  a = list(map(lambda x:x-1, a))
print(50)
print(" ".join(map(str, a)))