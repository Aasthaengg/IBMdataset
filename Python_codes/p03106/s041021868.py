def main():
    A, B, K = map(int, input().split())
    v = []
    for i in range(1, min([A, B])+1):
        if A % i == 0 and B % i == 0:
            v.append(i)
    print(v[-K])


if __name__ == '__main__':
    main()
