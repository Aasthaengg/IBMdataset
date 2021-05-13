# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N = int(input())
T,A = (int(i) for i in input().split())
H = list(map(int, input().split()))


#Hi mの気温
#T_H =[-100]*N
dif =[100]*N
for i in range(N):
    T_H =T -H[i] *0.006
    dif[i] =abs(T_H -A)

ans =dif.index(min(dif)) #最小値のインデックス
print(ans +1)