def main():
    N = int(input())
    ans = 0
    def c(i, j):
        res = 0
        str_i = str(i)
        str_j = str(j)
        for k in range(1, N+1):
            if str(k)[0] == str_i and str(k)[-1] == str_j:
                res += 1
        return res

    for i in range(1, 10):
        for j in range(1, 10):
            ans += c(i,j) * c(j, i)

    print(ans)
main()