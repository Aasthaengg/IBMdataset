def main():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.sort(reverse=True)
    ans =max(0, max(A) - sum(A[1:]) - 1)
    print(ans)

if __name__ == "__main__":
    main()