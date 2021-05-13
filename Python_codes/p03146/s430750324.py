def collatz_problem(s):
    a = []

    a.append(s)
    counter = 1
    while True:
        counter += 1
        if s % 2 == 0:
            s /= 2
            a.append(s)
        else:
            s = s * 3 + 1
            a.append(s)
        for i in range(len(a)-1):
            if a[i] == s:
                return counter


def main():

    s = int(input())
    answer = collatz_problem(s)
    print(answer)


if __name__ == "__main__":
    main()
