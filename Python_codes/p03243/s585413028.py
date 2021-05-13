# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
N = int(input())
num =[111,222,333,444,555,666,777,888,999]
for i in range(8):
    if N <= num[0]:
        ans =111
        break
    elif  num[i] < N <= num[i+1]:
        ans =num[i+1] 

print(ans)