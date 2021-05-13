def main():
    a,b = (int(x) for x in input().split())
    print('Odd' if a*b%2!=0 else 'Even')

if __name__ == '__main__':
    main()