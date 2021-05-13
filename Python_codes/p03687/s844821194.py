def main():
    S = input()
    ST = set(S)
    ans = 100
    for st in ST:
        count = 0
        T = list(S)
        tmp = ''
        while len(set(T)) > 1:
            for i in range(len(T) - 1):
                if st in [T[i], T[i + 1]]:
                    tmp += st
                else:
                    tmp += T[i]
            T = tmp
            tmp = ''
            count += 1
        ans = min(ans, count)
    print(ans)


if __name__ == '__main__':
    main()
