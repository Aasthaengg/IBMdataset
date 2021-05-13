n = int(input())
count = 0
preemos = []

is_prime = [True] * 55555
is_prime[0],is_prime[1] = False, False

for i in range(2, 55555):
  if count == n: break
  if is_prime[i]:
    if i % 10 == 1:
      count += 1
      preemos.append(i)
    for j in range(i, 55555, i):
      is_prime[j] = False
      
for i in preemos:
  print(i, end = " ")