def main():
    N = int(input())
    S = input()
    Ws = [0]*(N+1)
    Bs = [0]*(N+1)
    for i in range(1, N + 1):
        Bs[i] = Bs[i - 1] + (1 if S[i-1] == '#' else 0)
        Ws[N - i] = Ws[N + 1 - i] + (1 if S[N - i] == '.' else 0)
    # print(Ws[:10], Bs[:10])
    ans = Bs[0] + Ws[0]
    for i in range(1, N + 1):
        ans = min(ans, Bs[i] + Ws[i])
    print(ans)

if __name__ == '__main__':
    main()
