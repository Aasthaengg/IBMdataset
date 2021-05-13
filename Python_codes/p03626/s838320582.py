def solve():
    MOD = 1000000007

    N = int(input())
    S1 = input()
    S2 = input()

    patterns = []

    i = 0
    while i < N:
        if S1[i] == S2[i]:
            patterns.append(0)
            i += 1
        else:
            patterns.append(1)
            i += 2
    
    ans = 1
    for i in range(len(patterns)):
        c = 0
        if i == 0:
            if patterns[i] == 0:
                c = 3
            else:
                c = 6
            
            ans *= c
            ans %= MOD
            continue

        if patterns[i] == 0:
            if patterns[i-1] == 0:
                c = 2
            else:
                c = 1
        else:
            if patterns[i-1] == 1:
                c = 3
            else:
                c = 2
        
        ans *= c
        ans %= MOD
    
    print(ans)
    
if __name__ == '__main__':
    solve()
