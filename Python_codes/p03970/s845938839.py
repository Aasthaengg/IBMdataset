def solve():
    S = input()
    ans = 0
    for i, j in zip(S, "CODEFESTIVAL2016"):
        if i != j:
            ans += 1
    print(ans)
        
solve()