def main():
    n, k = map(int, input().split())
    A = [int(a) for a in input().split()]
        
    for i in range(n - k):
        if A[i + k] > A[i]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()