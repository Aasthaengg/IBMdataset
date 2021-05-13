def read_ints():
    return[int(i) for i in input().split()]

def main():
    d, n = read_ints()
    print(101 * (100**d) if n == 100 else (100**d)*n)

if __name__ == '__main__':
    main()