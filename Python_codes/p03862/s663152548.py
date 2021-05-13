def solve():
    N, X = map(int,input().split())
    A = [0] + list(map(int, input().split()))
    ans = 0
    #A =[]*N個、for i in range(N-1)でやると、初項がXより大きい場合に対応できない。
    #より正確にいうと、A =[3, 3, 2] X = 1のようなケース。 A1>A3かつ A1+A2>X かつ　A2+A3 > Xのとき
    for i in range(N):
        diff = A[i] + A[i+1] - X
        if diff > 0:
            A[i+1] -= diff
            ans += diff
    print(ans)


if __name__ == '__main__':
    solve()
