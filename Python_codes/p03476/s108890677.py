data = sorted(list(range(10**5+1)))
prime_bool = [True]*(10**5+1)
prime_bool[0] = False
prime_bool[1] = False
for i in range(2, len(data)):
  p = data[i]
  if prime_bool[p]:
    k = 2
    while k*p <= 10**5:
      prime_bool[k*p] = False
      k += 1

count_list = [0]*(10**5+1)
for i in range(1, 10**5+1):
  count_list[i] = count_list[i-1]
  if prime_bool[i] and prime_bool[(i+1)//2]:
    count_list[i] += 1

q = int(input())
for i in range(q):
  l,r=map(int, input().split())
  print(count_list[r]-count_list[l-1])
  
