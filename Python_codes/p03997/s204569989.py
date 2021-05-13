def main():
    a,b,h = (int(input()) for _ in range(3))
    print((a+b)*h//2)

if __name__ == '__main__':
    main()