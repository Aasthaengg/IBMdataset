def main():
    x,a,b = (int(input()) for _ in range(3))
    print((x-a)%b)

if __name__ == '__main__':
    main()