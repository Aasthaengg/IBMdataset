n = int(input())
n2 = int(n ** 0.5) + 1
n3 = n * 1
ans = 0

def md(r):
    divisors = []
    for i in range(1, int(r**0.5)+1):
        if r % i == 0:
            divisors.append(i)
            if i != r // i:
                divisors.append(r//i)

    # divisors.sort()
    return divisors

a = set(md(n-1))

for i in range(2,n2+1):
    n3 = n * 1
    while True:
        if n3 % i == 0:
            n3 //= i
        else:
            n3 %= i
            if n3 == 1:
                a.add(i)
            break
    
if n != 2:
    print(len(a))
else:
    print(1)