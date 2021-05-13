def main():
    a,b,c = (int(x) for x in input().split())
    print('Yes' if a <= c <= b else 'No')

if __name__ == '__main__':
    main()