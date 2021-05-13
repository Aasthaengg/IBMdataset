A, B, K = list(map(int, input().split()))
Co = [A, B]

for i in range(K):
  if Co[i % 2] % 2 == 1:
    Co[i % 2] -= 1
  Co[i % 2] /= 2
  Co[(i+1) % 2] += Co[i % 2]

Co = list(map(int, Co))
print(Co[0], Co[1])