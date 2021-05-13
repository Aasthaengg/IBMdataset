def main():
    N, A, B = (int(i) for i in input().split())
    X = [int(i) for i in input().split()]
    ans = 0
    for i in range(N-1):
        dist = X[i+1] - X[i]
        ans += min(A*dist,B)
    print(ans)

if __name__ == '__main__':
    main()