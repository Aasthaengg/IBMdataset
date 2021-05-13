def main():
    a,b,c = (int(x) for x in input().split())
    print(min(a+b,a+c,b+c))

if __name__ == '__main__':
    main()