def resolve():
    N = int(input())
    S = input()
    ans = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(N-1):
        X = S[:i+1]
        Y = S[i+1:]
        count = 0
        for j in abc:
            if j in X and j in Y:
                count += 1
        ans.append(count)
    print(max(ans))
resolve()