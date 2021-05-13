def main(X, N, p):
    for d in range(X + 2):
        if not((X - d) in p):
            print(X - d)
            return
        elif not((X + d) in p):
            print(X + d)
            return


if __name__ == "__main__":
    X, N = [int(s) for s in input().split(' ')]
    input_s = input()
    p = []
    if input_s != "":
        p = [int(s) for s in input_s.split(' ')]
    main(X, N, p)
