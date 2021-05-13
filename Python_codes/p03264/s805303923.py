# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない

K = int(input())
od =(K+1)//2
ev =K//2
ans =od *ev
print(ans)