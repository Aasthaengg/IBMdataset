def main():
    n = int(input())
    max, dif = 0, 0
    for i in range(1, 10000):
        s = i * (i + 1) // 2
        if s >= n:
            max = i
            dif = s - n
            break
    [print(i) for i in range(1, max + 1) if i != dif]

if __name__ == '__main__':
    main()
