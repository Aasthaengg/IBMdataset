def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a_s = set(a)
    if len(a) == len(a_s):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()