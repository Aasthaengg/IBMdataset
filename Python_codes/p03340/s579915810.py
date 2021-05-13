N = int(input())
A = list(map(int,input().split()))

li,ri = 0,0
ans = 0
xor = A[li]
add = A[li]
while ri < N and li <= ri:
    if xor == add: # 問題条件の判定
        ans += ri - li +1   # 先頭を固定したときの組み合わせの数(e.g. 1234,123,12,1)
        ri += 1
        if ri < N:  # 境界値の判定・・・別にすると読みやすい
            xor ^= A[ri]
            add += A[ri]
    else:
        if li < N:
            xor ^= A[li]
            add -= A[li]
        li += 1

print(ans)