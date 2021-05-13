def main():
    n,a,b = (int(x) for x in input().split())
    print(min(b,a*n))

if __name__ == '__main__':
    main()