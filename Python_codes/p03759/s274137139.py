def main():
    t = list(map(int, input().split()))
    if t[1] - t[0] == t[2] - t[1]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()