def main():
    a, b, c = map(int, input().split())
    k = int(input())
    p = pow(2, k)
    print(a + b + c - max(a,b,c) + max(a,b,c)*p)

if __name__ == '__main__':
    main()