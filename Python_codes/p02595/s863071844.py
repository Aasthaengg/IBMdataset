def main(X, Y, D):
    length = X**2 + Y**2
    if length <= D**2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        ans += main(X, Y, D)
    print(ans)

