import math
x=int(input())

def get_sieve_of_eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

data = get_sieve_of_eratosthenes(x*2)
for i in data:
  if i>=x:
    print(i)
    break
#print(data)