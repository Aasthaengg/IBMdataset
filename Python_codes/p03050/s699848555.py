N = int(input())

#約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
         if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    #divisors.sort()
    return divisors

ans_list = list()
divisors = make_divisors(N)

for p in divisors:
    if p!= N:
        m = N//p - 1
        if N//m == N%m:
            ans_list.append(m)
    
print(sum(ans_list))