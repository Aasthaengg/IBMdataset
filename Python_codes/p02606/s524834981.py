def main():
    l, r, d = map(int, input().split())
    a = (l-1)//d
    b = r//d
    print(b-a)

if __name__ == '__main__':
    main()
