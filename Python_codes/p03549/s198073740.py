def main():
    N, M = (int(i) for i in input().split())
    p_ac = (1/(2**M))
    p_wa = 1 - p_ac
    ans = 0
    exe_time = 1900*M + 100*(N-M)
    for k in range(1, 10**5)[::-1]:
        ans += k * (exe_time) * p_ac * (p_wa**(k-1))
    print(round(ans))


if __name__ == '__main__':
    main()
