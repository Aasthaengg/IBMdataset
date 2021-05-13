# 初期入力
import sys
input = sys.stdin.readline
b =input().strip()
ans =""
if b=="A":
    ans="T"
elif b =="T":
    ans ="A"
elif b =="C":
    ans ="G"
elif b =="G":
    ans ="C"
print(ans)