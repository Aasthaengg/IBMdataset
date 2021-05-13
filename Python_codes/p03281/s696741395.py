def f(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: divisors.append(n//i)
    divisors.sort()
    return divisors
print(len([i for i in range(1,int(input())) if(i+1)%2==1 and len(f(i+1))==8]))