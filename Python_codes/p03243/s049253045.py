x = [i * 111 for i in range(1, 10)]
N = int(input())
for j in range(len(x)):
  if 0 <= x[j] - N <= 110:
    print(x[j])
    break
