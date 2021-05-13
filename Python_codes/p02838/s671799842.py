def main():
    n = int(input())
    A = list(map(int, input().split()))
    M = max(A)
    dig = len(bin(M)) - 2
    MOD = 10 ** 9 + 7
    ans = 0
    d = {i: [0, 0] for i in range(dig)}
    for a in A:
        a = bin(a)[2:].zfill(dig)
        for i in range(len(a)):
            if a[-(i+1)] == '0':
                d[i][0] += 1
            else:
                d[i][1] += 1
    for i in range(dig):
        ans += d[i][0] * d[i][1] * pow(2, i, MOD)
        ans %= MOD
    print(ans)
main()
