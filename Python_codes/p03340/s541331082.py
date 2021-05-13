# D - Xor Sum 2

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

l,r = 0,1 # l<rの場合を考える
tmp_xor = A[l] ^ A[r]
tmp_sum = A[l] + A[r]
ans = N

while 1:
    if tmp_xor == tmp_sum:
        ans += r-l # 先頭l以上、末尾rの部分数列の個数
        r += 1
        if r == N:
            break
        tmp_xor = tmp_xor ^ A[r]
        tmp_sum += A[r]
    elif l+1 < r:
        tmp_sum -= A[l]
        tmp_xor = tmp_xor ^ A[l]
        l += 1
    else:
        l = r
        r += 1
        if r == N:
            break
        tmp_xor = A[l] ^ A[r]
        tmp_sum = A[l] + A[r]

print(ans)