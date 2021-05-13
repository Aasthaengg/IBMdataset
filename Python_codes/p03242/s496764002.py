# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
n =input().strip()
ans =""
for i in n:
    if i=="1":
        ans +="9"
    elif i=="9":
        ans +="1"
print(ans)