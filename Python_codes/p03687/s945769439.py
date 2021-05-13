S = input()
ans = float('inf')
for s in S:
    T = (S + 'a')[:-1]
    # print(id(S) == id(T))
    cnt = 0
    while T.count(s) < len(T):
        D = []
        for i in range(len(T)-1):
            D.append(s if T[i] == s or T[i+1] == s else T[i])
        T = ''.join(D)
        # print(T)
        cnt += 1
    ans = min(ans, cnt)
print(ans)
