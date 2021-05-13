amari1 = []
amari2 = []
amari3 = []
amari4 = []

prime = [True] * 55556
prime[0] = False
prime[1] = False
for i in range(2, 55556):
  if not prime[i]:
    continue
  now = i
  while now + i <= 55555:
    now += i
    prime[now] = False
    
for i in range(2, 55556):
  if prime[i] == True:
    amari = i % 5
    if amari == 1:
      amari1.append(i)
    elif amari == 2:
      amari2.append(i)
    elif amari == 3:
      amari3.append(i)
    elif amari == 4:
      amari4.append(i)

N = int(input())
print(' '.join(map(str, amari1[:N])))
