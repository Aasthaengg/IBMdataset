#約数の個数の和（１~N）約数そのものを求めないので「速い」
def divisor_num(N):
    ans =0
    for i in range(1,N):
        ans +=(N-1)//i #項数
    return ans


# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない

N = int(input())
ans =divisor_num(N)

print(ans)