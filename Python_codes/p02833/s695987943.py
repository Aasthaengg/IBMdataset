N = int(input())

# N:奇数ならば0
# N:偶数の場合 10が何個登場するか (素因数分解したときに2,5のペアが何個登場するか)
# 偶数の場合のみ考えているので 5 << 2と考えて5が何回登場するかを考える。
# 2で割ると(N//2)!になる
# 5 >> 2を仮定するとN//2までの5の倍数となっている数が答え。。。では無い
# 5の2乗,3乗の倍数をカウントできていないのでそれらを足す？
if N % 2 != 0:
    print(0)
    exit()

cnt = 0
current = 5
while (N // 2 >= current):
    cnt += (N // 2 // current)
    current *= 5

print(cnt)