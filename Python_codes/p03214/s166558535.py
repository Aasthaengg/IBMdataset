def main():
    n = int(input())
    A = list(map(int, input().split()))
    m = sum(A) / n
    A = [abs(a - m) for a in A]
    print(A.index(min(A)))

if __name__ == '__main__':
    main()
