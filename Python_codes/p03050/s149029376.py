def main():
    def trial_division(n):
        divs = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.append(i)
                if i != n//i:
                    divs.append(n//i)
        return divs

    N = int(input())
    divs = trial_division(N)
    ans = 0
    for d in divs:
        if d != 1 and N//(d-1) == N % (d-1):
            ans += (d-1)
    print(ans)


if __name__ == '__main__':
    main()
