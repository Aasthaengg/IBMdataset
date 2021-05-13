def divisible(n) :
    divisors = []
    for i in range(1, int(n ** 0.5) + 1) :
        if n % i == 0 :
            divisors.append(i)
            if i != n // i :
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors

N, K = map(int,input().split())
xs = list(map(int,input().split()))
divs = divisible(sum(xs))

for div in divs :
    test = [x % div for x in xs]
    test.sort()
    sum_test = sum(test)
    change = sum(test[:-sum_test//div])
    if change <= K :
        ans = div
        break
print(ans)

