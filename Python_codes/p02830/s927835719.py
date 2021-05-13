def resolve():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

if '__main__' == __name__:
    resolve()