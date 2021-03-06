


N = int(input())

"""
愚直にやると、Kを2～Nの範囲で全部調べて数え上げる。N <= 10**12 なので間に合わない。


たとえば N=100だと、
[2, 3, 4, 9, 10, 11, 33, 99, 100]
が条件を満たす数字になる。

割り算を行わないとき、明らかに N % K = 1 になる
これは、「NをKで割ったら、１あまる」であるから、「N-1をKでわったら割り切れる」ともいえる。
なので、割り算が起こらないものは、N-1の約数。

割り算が起こるやつは、割れるだけ割った後、余りを調べればよい。
"""



def solve(n):
    i = 1
    ret = set()
    while i * i <= n:
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
        i += 1

    return ret


div_N_sub_1 = solve(N-1)
div_N = solve(N)

ans = len(div_N_sub_1) - 1

for i in div_N:
    if i == 1:
        continue
    tmp = N
    while tmp % i == 0:
        tmp //= i
    if tmp % i == 1:
        ans += 1


print(ans)