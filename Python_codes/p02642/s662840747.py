def resolve():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    import collections
    counter = collections.Counter(A)
    maxA = max(A)
    dp = [True for _ in range(max(A)+1)]
    for a in A:
        if counter[a] > 1:
            dp[a] = False
        for j in range(a+a, maxA+1, a):
            dp[j] = False
    #print(dp)
    print(sum(1 for a in A if dp[a]))

if '__main__' == __name__:
    resolve()