#計算でもとまるのか・・・
# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
#*S, = input() 
S =input().strip()
c1 =S.count("1")
c0 =S.count("0")
print(min(c0,c1)*2)