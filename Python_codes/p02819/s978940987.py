def prime_list():
  p_lis = [True] * (2 * 10**5 + 1)
  p_lis[0], p_lis[1] = False, False
  for i in range(2, 2 * 10**5 + 1):
    if p_lis[i]:
      j = 2
      while j * i <= 2 * 10**5:
        p_lis[j*i] = False
        j += 1
  return p_lis

x = int(input())
p_lis = prime_list()
j = 0
while True:
  if p_lis[x+j]:
    print(x+j)
    break
  j += 1

