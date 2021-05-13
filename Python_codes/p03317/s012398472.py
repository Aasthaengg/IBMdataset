import math

def read_ints():
    return[int(i) for i in input().split()]

def main():
    n, k = read_ints()
    print(math.ceil((n - 1) / (k - 1)))

if __name__ == '__main__':
    main()