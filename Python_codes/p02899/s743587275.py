def some():
    n = int(input())
    h = map(int, input().split(" "))
    h = sorted((i, index) for index, i in enumerate(h, 1))
    print(" ".join(str(num) for _, num in h))
some()