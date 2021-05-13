from collections import Counter
def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a
n = int(input())
input_list = list(map(int,input().split()))
num_count = Counter([prime for num in input_list for prime in prime_factorize(num)])
if len(num_count.values())==0:
    print("pairwise coprime")
    exit()
max_appear = max(num_count.values())
if max_appear == 1:
    print("pairwise coprime")
elif max_appear != n:
    print("setwise coprime")
else:
    print("not coprime")