def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = A.pop()
    B = [[a, abs(a - (m / 2))] for a in A]
    B.sort(key = lambda x: x[1])
    print('{} {}'. format(m, B[0][0]))

if __name__ == '__main__':
    main()
