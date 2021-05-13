def main():
    inp = lambda: [int(x) for x in input().split()]    
    n, k = inp()
    a = inp()
    min_a = min(a)
    dp = [False] * (k+1)
    for i in range(k + 1):
        if i < min_a:
            dp[i] = False
        elif i in a:
            dp[i] = True
        else:
            for j in a:
                if i >= j and not dp[i-j]:
                    dp[i] = True
                    break

    ans = "First" if dp[k] else "Second"
    print(ans)


if __name__ == '__main__':
    main()
