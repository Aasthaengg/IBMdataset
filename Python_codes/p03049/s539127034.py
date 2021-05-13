def solve():
    N = int(input())
    s = []
    ans = 0

    A_cnt = 0
    B_cnt = 0
    BA_cnt = 0
    for i in range(N):
        s_tmp = input()
        s.append(s)
        for j in range(len(s_tmp)-1):
            if s_tmp[j] == "A" and s_tmp[j+1] == "B":
                ans += 1
        
        if s_tmp[0] == "B" and s_tmp[-1] == "A":
            BA_cnt += 1
        elif s_tmp[0] == "B":
            B_cnt += 1
        elif s_tmp[-1] == "A":
            A_cnt += 1
    
    if BA_cnt > 0:
        ans += BA_cnt - 1
        if A_cnt > 0:
            A_cnt -= 1
            ans += 1
        if B_cnt > 0:
            B_cnt -= 1
            ans += 1
    
    ans += min(A_cnt,B_cnt)
    
    print(ans)
if __name__ == '__main__':
    solve()