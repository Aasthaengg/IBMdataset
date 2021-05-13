def main():
    a,b = (int(x) for x in input().split())
    c = [True for x in (a,b,a+b) if x%3==0]
    print('Possible' if c else 'Impossible')

if __name__ == '__main__':
    main()