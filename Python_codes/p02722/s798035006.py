def main():
    N = int(input())
    ans = set()

    def trial_division(n):
        divs = set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if i != 1:
                    divs.add(i)
                if i != n//i:
                    divs.add(n//i)
        return divs

    ans |= (trial_division(N))
    ans |= (trial_division(N-1))
    answer = 0
    for k in ans:
        cur = N
        while cur % k == 0 and cur != 1:
            cur //= k
        if cur == 1 or cur % k == 1:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
