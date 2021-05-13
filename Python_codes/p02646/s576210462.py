def main():
    import sys
    input = sys.stdin.readline
    A, V = [int(x) for x in input().strip().split()]
    B, W = [int(x) for x in input().strip().split()]
    T = int(input())
    if A == B:
        print('YES')
        return
    if W > V:
        print('NO')
        return
    if (V - W) * T >= abs(A - B):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()