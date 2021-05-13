def main():
    S = list(input())
    a = S.count('a')
    b = S.count('b')
    c = S.count('c')
    if a == b and b == c:
        print('YES')
    elif abs(a - b) > 1 or abs(b - c) > 1 or abs(a-c) > 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()