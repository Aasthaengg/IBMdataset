cache = {}

def main():
    def lucas(x):
        if x == 0:
            return 2
        elif x == 1:
            return 1
        elif x in cache:
            return cache[x]
        else:
            cache[x] = lucas(x-1) + lucas(x-2)
            return cache[x]

    N = int(input())
    print(lucas(N))


if __name__ == '__main__':
    main()
