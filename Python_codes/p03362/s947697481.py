def main():
    n = int(input())
    primes = get_primes(55555)
    out = []
    num = 0
    for prime in primes:
        if prime%5 == 1:
           out.append(prime)
           num += 1
        if n == num:
            print(*out)
            return

def get_primes(x):
    if x < 2: return []
    if x == 2: return [2]
    limit = x**0.5 + 1
    nums = list(range(3, x+1, 2))
    dividers = [2]
    divider = 3
    while limit > divider:
        dividers.append(divider)
        nums = [num for num in nums if num%divider]
        divider = nums[0]
    return dividers+nums
        
if __name__ == "__main__":
    main()