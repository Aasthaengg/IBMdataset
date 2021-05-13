def main():
    A,V = [int(x) for x in input().split()]
    B,W = [int(x) for x in input().split()]
    T = int(input())
    D = abs(A-B)
    if V<=W:
        print('NO')
        return
    F = V-W
    if D/F <= T:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()