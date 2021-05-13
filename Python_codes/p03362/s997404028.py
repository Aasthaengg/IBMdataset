n = int(input())
maxn = 55555
is_prime = [True if i%2 == 1 else False for i in range(0, maxn+1) ]
is_prime[0] = False
is_prime[1] = False
is_prime[2] = True # 2は素数
for i in range(3, int(maxn**0.5) + 1, 2):
    if not is_prime[i]:
        continue
    for j in range(i*2, maxn+1, i):
        is_prime[j] = False

ps = [i for i in range(maxn+1) if is_prime[i]]

a = [] 
i = 2
while True:
    if ps[i] % 5 == 1:
        a.append(ps[i])
    if len(a) == n:
        break
    i += 1

print(' '.join(map(str, a)))
