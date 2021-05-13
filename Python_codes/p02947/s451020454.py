def resolve():
    N = int(input())
    S = sorted(["".join(sorted(input())) for _ in range(N)])
    #print(S)
    ans = 0
    cnt = 0
    for i in range(1, N):
        if S[i-1] == S[i]:
            if cnt == 0:
                cnt = 2
            else:
                cnt += 1
        else:
            if cnt != 0:
                ans += cnt*(cnt-1)//2
            cnt = 0
    if cnt != 0:
        ans += cnt*(cnt-1)//2
    print(ans) 
    


    
if '__main__' == __name__:
    resolve()