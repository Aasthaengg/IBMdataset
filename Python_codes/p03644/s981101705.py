def actual(N):
    max_count = 0

    for n in range(1, N + 1):
        i = n

        count = 0

        while n % 2 == 0:
            count += 1
            n //= 2

        if count >= max_count:
            max_count = count
            answer = i

    return answer

N = int(input())
print(actual(N))