def main():
    S = list(map(int, list(input().rstrip())))
    K = int(input())
    if sum(S[:K]) == K and len(set(S[:K])) == 1:
        print(1)
    else:
        for s in S:
            if s != 1:
                print(s)
                exit()


if __name__ == '__main__':
    main()
