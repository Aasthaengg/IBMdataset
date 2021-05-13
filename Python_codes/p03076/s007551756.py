# 初期入力
import sys
input = sys.stdin.readline
a =[]
for i in range(5):
    x = int(input())
    x2 =x %10
    x3 =x
    #10分刻みにする
    x /= 10 
    if not x.is_integer():
        x=int(x)*10 +10
    else:
        x =int(x)*10
    if x2 ==0:
        x2 =10
    a.append((x2,x,x3))
a.sort(reverse=True)
ans =0
for i in range(4):
    ans +=a[i][1]
ans +=a[4][2]
print(ans)