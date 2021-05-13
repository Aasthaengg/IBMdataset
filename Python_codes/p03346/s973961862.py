import sys
input = sys.stdin.readline

# 抜き取るだけ抜き取ってから、自由に追加していくと思える
# 残す部分が「完成」している必要がある
# L,L+1,...,Rの左右が出来ているようなものを残せる

N = int(input())
P = [int(input()) for _ in range(N)]

p_to_i = {x:i for i,x in enumerate(P)}

max_rest = 1
# 各数字が右端に来るときの最大長を持つ
x = 1
for n in range(2,N+1):
    if p_to_i[n] > p_to_i[n-1]:
        x += 1
        if max_rest < x:
            max_rest = x
    else:
        x = 1

answer = N - max_rest
print(answer)