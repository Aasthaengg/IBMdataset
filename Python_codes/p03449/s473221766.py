def main():
    N = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    ans = 0; cnt = 0
    for i in range(N):
        cnt += sum(A1[:i]) + A1[i]
        cnt += sum(A2[i:])
        ans = max(ans, cnt)
        cnt = 0
    print(ans)

if __name__ == "__main__":
    main()
