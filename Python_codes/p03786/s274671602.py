def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = sorted([int(x) for x in input().strip().split()])

    def judge(i):
        m = A[i]
        for j, a in enumerate(A):
            if i == j:
                continue
            if a <= 2 * m:
                m += a
            else:
                return False
        return True
    
    l = -1
    r = N
    while l + 1 < r:
        m = (l + r) // 2
        if judge(m):
            r = m
        else:
            l = m
    
    print(N - (l + 1))

if __name__ == '__main__':
    main()