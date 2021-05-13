# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
#A,B,C = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans =A[0]*10 +A[1] +A[2]
print(ans)