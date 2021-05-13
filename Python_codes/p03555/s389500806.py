def main():
    c1,c2 = (input() for _ in range(2))
    if c1 == c2[::-1]: print('YES')
    else: print('NO')

if __name__ == '__main__':
    main()