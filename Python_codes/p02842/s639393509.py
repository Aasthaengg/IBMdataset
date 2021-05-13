# 初期入力　　２０２０－０７２７　21：50
import math
import sys
input = sys.stdin.readline  #文字列では使わない
N = int(input())
ans =":("
for i in range(1,50001):
    a =int( i *1.08 )
    if a==N:
        ans =i
        break
print(ans)