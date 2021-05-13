S = list(input())
K = int(input())

N = len(S)

if len(set(S)) == 1: #種類が１つ
    tmp = K * N // 2
    print (tmp)
    exit()

if S[0] != S[-1]:
    count = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            S[i + 1] = '*'
            count += 1
    print (count * K)
else:
    i = 1
    while i < N:
        if S[i - 1] != S[i]:
            break
        i += 1
    
    j = 1
    while j < N:
        if S[N - j] != S[N - j - 1]:
            break
        j += 1
    
    ans = 0
    tmp = 1
    for k in range(i, N - j):
        if S[k] != S[k + 1]:
            ans += K * (tmp // 2)
            tmp = 1
        else:
            tmp += 1
    ans += K * (tmp // 2)
    ans += (K - 1) * ((i + j) // 2)
    ans += i // 2
    ans += j // 2
    print (ans)