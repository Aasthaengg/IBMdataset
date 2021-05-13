def primes(n):
    if n == 2:
        return [2]
    nums = list(range(2, n + 1))
    primes = list()
    while len(nums) > 0:
        primes.append(nums[0])
        tmp = list()
        for n in nums[1:]:
            if n % nums[0] > 0:
                tmp.append(n)
        nums = tmp
    return primes


def main():
    N = int(input())
    ps = primes(10000)
    ans = list()
    for p in ps:
        if p % 5 != 1:
            continue
        ans.append(p)
        if len(ans) >= N:
            break
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()