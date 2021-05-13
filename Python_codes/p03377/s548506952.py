def main():
    line = input()
    A, B, X = [int(n) for n in line.split()]
    if A > X:
        print('NO')
    elif B + A < X:
        print('NO')
    else:
        print('YES')

main()
