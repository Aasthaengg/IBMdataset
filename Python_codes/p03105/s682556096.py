# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
A,B,C = map(int, input().split())
hear =B //A
ans =min(hear,C)
print(ans)