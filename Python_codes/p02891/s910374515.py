def main():
    S = input()
    K = int(input())
    ans = 0
    L = len(S)
    s = set([i for i in S])
    if len(s) == 1:
        print((L*K)//2)
        exit()
    cnt = 1
    for i in range(L):
        if i < L-1 and S[i] == S[i+1]:
            cnt += 1
        else:
            ans += cnt//2
            cnt = 1
    ans *= K
    if S[0] == S[-1]:
        t = S[0]
        i = 0
        a = 0
        b = 0
        while i < L and S[i] == t:
            a += 1
            i += 1

        i = L-1
        while i >= 0 and S[i] == t:
            b += 1
            i -= 1

        tmp = a//2+b//2-(a+b)//2
        tmp *= (K-1)
        ans -= tmp
    print(ans)
if __name__ == "__main__":
    main()
