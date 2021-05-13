def main():
    a, b = input().split()
    a = int(a)
    b_1 = ''
    b_1 += b[0]
    b_1 += b[2:]
    b_1 = int(b_1)

    answer = (a * b_1) // 100
    print(answer)


if __name__ == '__main__':
    main()