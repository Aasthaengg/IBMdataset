def solve():

    X = list(map(int, input().split()))

    X = sorted(X, reverse=True)

    X_max = max(X) #A~Cの内、最大のもの
    n = 0

    while X[0] > X[1]:
        X[1] += 1
        n += 1
    while X[0] > X[2]:
        X[2] += 1
        n += 1
    if n%2 == 1:
        n += 3

    ans =int(n / 2)

   # print(X)
    print(ans)
    
    

if __name__ == "__main__":
    solve()
