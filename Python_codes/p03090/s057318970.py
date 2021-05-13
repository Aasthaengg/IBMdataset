def main():
    N = int(input())
    edges = []
    M = N*(N-1)//2 - N//2
    
    if N%2 == 1:
        for i in range(1, N):
            for j in range(i+1, N+1):
                if i + j != N:
                    edges.append((i, j))
    else:
        for i in range(1, N):
            for j in range(i+1, N+1):
                if i + j != N + 1:
                    edges.append((i, j))
    print(M)
    for a, b in edges:
        print(a, b)
if __name__ == "__main__":
    main()