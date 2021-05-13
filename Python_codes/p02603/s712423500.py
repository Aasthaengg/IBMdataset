def main():
    N = int(input())
    A = list(map(int, input().split()))
    current = 1000
    prev = A[0]
    for a in A[1:]:
        if prev < a:
            n = current // prev
            current = a * n + (current % prev)
        prev = a
    print(current)


if __name__ == "__main__":
    main()
