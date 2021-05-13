# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
S =input().strip()
dif =[]
for i in range(len(S)-2):
    x =abs(int(S[i:i+3]) -753)
    dif.append(x)
print(min(dif))