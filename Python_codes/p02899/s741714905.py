def main():
    N = input()
    A = [(a, idx) for idx, a in enumerate(map(int, input().split()), start=1)]
    A.sort(key = lambda x: x[0])
    print(" ".join([str(a[1]) for a in A]))


if __name__ == '__main__':
    main()
