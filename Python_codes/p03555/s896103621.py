def main():
    a = list(input())
    b = list(input())
    if a[0] == b[2] and a[2] == b[0] and a[1] == b[1]:
        print('YES')
    else:
        print('NO')
main()