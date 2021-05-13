def resolve():
  N, M, C = map(int, input().split(" "))
  B = [int(x) for x in input().split(" ")]

  counter = 0
  for _ in range(N):
    A = [int(x) for x in input().split(" ")]
    sum_of_a_x_b = 0
    for a, b in zip(A,B):
      sum_of_a_x_b += a * b
    if sum_of_a_x_b + C > 0:
      counter += 1
  print(counter)

if __name__ == "__main__":
  resolve()