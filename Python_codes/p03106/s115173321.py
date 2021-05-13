#公約数を求める
def cf(x1,x2):
    cf=[]
    for i in range(1,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
A,B,K = map(int, input().split())

#公約数
div =cf(A,B)


print(div[-K])