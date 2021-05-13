def main():
    def trial_division(n):
        divs = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.append(i)
                if i != n//i:
                    divs.append(n//i)
        divs.sort(reverse=True)
        return divs

    N, M = (int(i) for i in input().split())
    divs = trial_division(M)
    for d in divs:
        if N*d <= M:
            return print(d)


if __name__ == '__main__':
    main()
