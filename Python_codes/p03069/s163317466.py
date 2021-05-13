def main():
    N = int(input())
    S = list(input())

    #f len(set(S)) == 1:
    #    print(0)
     #   return

    baseblack = 0
    basewhite = sum([1 for x in S if x == '.'])
    ans = min(basewhite, N-basewhite)
    for i in range(N):
        baseblack += S[i] == '#'
        basewhite -= S[i] == '.'
        ans = min(ans, baseblack+basewhite)

    print(ans)

if __name__ == "__main__":
    main()
