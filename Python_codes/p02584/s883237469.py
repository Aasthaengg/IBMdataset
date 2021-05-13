def solve():
    X,K,D = [int(i) for i in input().split()]
    abs_X = abs(X)
    if D*K <= abs_X:
        print(abs_X - D*K)
    else:
        steps2pivot = abs_X // D
        abs_X -= steps2pivot * D
        rest = K - steps2pivot
        if rest % 2 == 0:
            print(abs_X)
        else:
            print(abs(abs_X-D))

if __name__ == "__main__":
    solve()