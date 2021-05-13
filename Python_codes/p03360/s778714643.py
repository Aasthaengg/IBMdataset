def main():
    t = list(map(int, input().split()))
    n = input()
    for i in range(int(n)):
        ind = t.index(max(t))
        t[ind] = t[ind] * 2
    print(sum(t))

if __name__ == '__main__':
    main()
