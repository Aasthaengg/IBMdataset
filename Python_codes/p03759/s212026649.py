def main():
    a,b,c = (int(x) for x in input().split())
    print('YES' if b-a == c-b else 'NO')

if __name__ == '__main__':
    main()