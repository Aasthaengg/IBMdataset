def main():
    a,b,x = (int(x) for x in input().split())
    print('YES' if b>=(x-a) and a<=x else 'NO')

if __name__ == '__main__':
    main()