def main():
    N = int(input())
    B = [float('inf')] + list(map(int, input().split())) + [float('inf')]
    A = []
    for i in range(N):
        A.append(min(B[i], B[i+1]))
    print(sum(A))

if __name__ == "__main__":
    main()
