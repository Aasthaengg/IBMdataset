def solution():

    n, m, d = map(int, input().split())


    if d == 0:
        guess = n
        return (m-1)/n

    else:

        guess = 2 * (n - d)
        return (guess*(m-1)/n**2)

print(solution())