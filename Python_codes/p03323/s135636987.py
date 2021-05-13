def main():
    a,b = (int(x) for x in input().split())
    print('Yay!' if a<=8 and b<=8 else ':(')

if __name__ == '__main__':
    main()