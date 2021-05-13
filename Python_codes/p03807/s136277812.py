def main():
    N = int(input())
    A = list(map(int,input().split()))
    n_odd = len([A[i] for i in range(N) if A[i]%2 != 0])
    n_even = N - n_odd
    if n_odd%2 != 0:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()