def main():
    X = int(input())
    maxi = 1
    if X <= 2:
        print(1)
        return
    for b in range(2, X):
        for p in range(2, X):
            if b**p > X:
                break
            else:
                maxi = max(maxi, b**p)
    print(maxi)
main()