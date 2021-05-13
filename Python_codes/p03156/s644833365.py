def resolve():
    n = int(input())
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    low, mid, high = 0, 0, 0
    for pi in p:
        if pi <= a:
            low += 1
        elif a + 1 <= pi <= b:
            mid += 1
        else:
            high += 1
    print(min(low, mid, high))


if __name__ == "__main__":
    resolve()
