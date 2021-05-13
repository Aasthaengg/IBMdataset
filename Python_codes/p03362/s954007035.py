def main():
    result = []
    counter = 0

    primes = [2]
    nominee = 3
    while counter < 55:
        is_prime = True
        for prime in primes:
            if nominee % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(nominee)
            if nominee % 5 == 1:
                result.append(nominee)
                counter += 1
        nominee += 2
    
    print(*result[:int(input())])
    

main()
