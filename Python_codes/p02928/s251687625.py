def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  maxA = max(A)
  base = 10**9+7
  # counter_of_A = [0]*(maxA+1)
  integra_of_counter = [0]*(maxA+1)

  # A の転倒数を数える。
  inversion_num_of_first_A = 0
  for a in reversed(A):
    if a > 1:
      inversion_num_of_first_A += integra_of_counter[a-1]
    
    for x in range(a, maxA+1):
      integra_of_counter[x] += 1


  # B の 2 番目の転倒数を数える
  inversion_num_of_second_A = 0
  for a in reversed(A):
    if a > 1:
      inversion_num_of_second_A += integra_of_counter[a-1]
    
    for x in range(a, maxA+1):
      integra_of_counter[x] += 1
  # print(integra_of_counter)
  # print(inversion_num_of_second_A)

  # print("K =", K, "a =", inversion_num_of_first_A, "d =", inversion_num_of_second_A - inversion_num_of_first_A)
  if K%2 == 0:
    result = K//2 * (2*inversion_num_of_first_A%base + (K-1)*(inversion_num_of_second_A - inversion_num_of_first_A)%base)
  else:
    result = (inversion_num_of_first_A%base + ((K-1)*(inversion_num_of_second_A - inversion_num_of_first_A)//2)%base)*K
  result %= base

  print(result)

if __name__ == "__main__":
  resolve()