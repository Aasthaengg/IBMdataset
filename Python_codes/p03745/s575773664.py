N = int(input())
A = list(map(int, input().split()))

ans = 1
flg = 0
rev = 0 # 0:単調非増加、1:単調非減少
for c,n in zip(A, A[1:]):
    
    if not flg:
        if c < n:
            # 単調非増加を仮定する
            flg = 1
        elif c > n:
            # 単調非減少を仮定する
            flg = 1
            rev = 1
    else:
        if rev:
            c = -c
            n = -n

        if c > n:
            ans += 1
            flg = 0
            rev = 0
            
print(ans)