
def prime_factor(n):
    ass = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass


n = int(input())
n_prime = {}
for i in range(1, n+1):
    for item in prime_factor(i):
        if item not in n_prime.keys():
            n_prime[item] = 0
        n_prime[item] += 1
#print(n_prime)
count_74 = 0
count_24 = 0
count_14 = 0
count_4 = 0
count_2 = 0
for prime, count in n_prime.items():
    if count >= 74:
        count_74 += 1
    if count >= 24:
        count_24 += 1
    if count >= 14:
        count_14 += 1
    if count >= 4:
        count_4 += 1
    if count >= 2:
        count_2 += 1
ans75 = count_74
ans25 = count_24*(count_2 - 1)
ans15 = count_14*(count_4 - 1)
ans5 = count_4*(count_4 - 1)*(count_2 - 2)//2
print(ans75 + ans25 + ans15 + ans5)
