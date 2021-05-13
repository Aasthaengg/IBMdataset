def main():
    K,T = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(T):
        ans = max(ans,2*A[i]-1-K)
    print(ans)

if __name__ == "__main__":
    main()