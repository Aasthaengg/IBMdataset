# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
N = int(input())
en =0
bt =0
for i in range(N):
    a,b =input().split()
    if b =="JPY":
        en +=float(a)
    elif b =="BTC":
        bt +=float(a)
ans =en +bt *380000.0
print(ans)