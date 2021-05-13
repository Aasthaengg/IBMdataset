def main():
    X, Y = map(int, input().split())
    cnt = 1
    for i in range(Y):
        X = 2*X
        if X <= Y:
            cnt += 1
        else:
            break
    print(cnt)
if __name__ == "__main__":
    main()