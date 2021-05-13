N = int(input())
S1 = list(input())
S2 = list(input())

if N == 1:
    print(3)
else:
    if S1[0] == S1[1]:
        left_domino = 0
        ans, i = 6, 2    
    else:
        left_domino = 1
        ans, i = 3, 1

    while i < N-1:
        if S1[i] == S1[i+1]:
            if left_domino == 0:
                ans *= 3
            else:
                ans *= 2
            left_domino = 0
            i += 2
        else:
            if left_domino != 0:
                ans *= 2
            left_domino = 1
            i += 1

    if S1[-1] == S2[-1] and left_domino != 0:
        ans *= 2

    print(ans % 1000000007)