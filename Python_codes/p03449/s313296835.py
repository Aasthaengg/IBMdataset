def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    A = [list(mi()) for _ in range(2)]
    m = -1
    for i in range(N):
        m = max(m, sum(A[0][:i+1])+sum(A[1][i:]))
    print(m)

if __name__ == '__main__':
    main()