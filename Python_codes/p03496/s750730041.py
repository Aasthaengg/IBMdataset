def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = []
    if max(A) + min(A) >= 0:
        x = A.index(max(A))
        for i in range(N):
            C.append((x+1, i+1))
        for i in range(1, N):
            C.append((i, i+1))
    else:
        x = A.index(min(A))
        for i in range(N):
            C.append((x+1, i+1))
        for i in range(N, 1, -1):
            C.append((i, i-1))
    print(len(C))
    for x, y in C:
        print(x, y)

if __name__ == "__main__":
    main()
