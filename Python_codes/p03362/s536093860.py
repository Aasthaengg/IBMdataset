def check_prime(k):
    '''
    素数の時1、合成数の時0を返す
    '''
    if k == 1:return 0
    num = int(k ** 0.5 // 1)
    for i in range(2, num + 1):
        if k % i == 0:return 0
    return 1

n = int(input())
prime = []

for i in range(2, 55556):
    if check_prime(i):
        prime.append(i)

rec = [2]
ind = 1
for i in range(n - 1):
    while True:
        if prime[ind] % 5 == 1:
            rec.append(prime[ind])
            ind += 1
            break
        ind += 1

print(*rec)