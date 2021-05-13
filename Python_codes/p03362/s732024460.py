def main():
    n = int(input())
    primes = get_primes_less_than(55556)
    out = []
    num = 0
    for prime in primes:
        if prime%5 == 1:
           out.append(prime)
           num += 1
        if n == num:
            print(*out)
            return

def get_primes_less_than(x):
    ans = []
    if x < 3:
        return ans
    if x == 3:
        ans.append(2)
        return ans
    else:
        for i in range(3, x, 2):
            for j in ans:
                if not i%j:
                    break
            else:
                ans.append(i)
    return ans
        
if __name__ == "__main__":
    main()