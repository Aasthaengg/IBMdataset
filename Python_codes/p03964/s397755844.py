def main():
    N = int(input())
    A, B = 1, 1
    for _ in range(N):
        t, a = (int(i) for i in input().split())
        mul = max(-(-A//t), -(-B//a))
        A = t*mul
        B = a*mul
    print(A+B)


if __name__ == '__main__':
    main()
