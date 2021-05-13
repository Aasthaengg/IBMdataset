def resolve():
    N = int(input())
    S = [list(input()) for _ in range(2)]
    i = 0
    ans = 1
    prev_color = 0
    while i < N:
        if S[0][i] == S[1][i]:
            ans *= 3 - prev_color
            prev_color = 1
            i += 1
        else:
            if prev_color == 0:
                ans *= 6
            elif prev_color == 1:
                ans *= 2
            else:
                ans *= 3 
            prev_color = 2
            i += 2
    print(ans%(10**9+7))
    


        

if '__main__' == __name__:
    resolve()