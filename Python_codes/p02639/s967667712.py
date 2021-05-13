def main(X):
    for i in range(len(X)):
        if X[i]==0:
            return i+1

if __name__ == '__main__':
    X = list(map(int, input().split()))
    ans = main(X)
    print(ans)

