def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dict = {}
    ans = 0
    for i in range(N):
        if S[i] in dict:
            continue
        else:
            dict[S[i]] = 1
            ans += 1

    return ans

print(main())
