def main():
    c = [input() for _ in range(3)]
    s = ''.join(c[i][i] for i in range(3))
    print(s)


if __name__ == '__main__':
    main()
