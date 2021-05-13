def main():
    n = int(input())
    s = list(input().split())
    res = len(set(s))
    if res == 4:
        print('Four')
    else:
        print('Three')

if __name__ == '__main__':
    main()