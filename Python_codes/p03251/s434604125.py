# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N,M,X,Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
f1=False
f2=False

#
ans ="War"
for Z in range(-100,101):
    f1=False
    f2=False
    if X < Z <Y:
        f1 =True
    if x[-1] < Z <=y[0]:
        f2 =True
    if f1 ==f2 ==True:
        ans ="No War"
        break
print(ans)