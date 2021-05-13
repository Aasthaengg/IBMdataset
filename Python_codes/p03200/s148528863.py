def resolve():
    S = input()
    Wcount = 0
    ans = 0
    for i in range(len(S)):
        if S[i] == 'W':
            ans += i-Wcount 
            Wcount += 1
    print(ans)
resolve()