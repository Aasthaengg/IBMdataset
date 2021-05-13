# 初期入力
import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
a.sort()
ans =a[0] *a[1] //2
print(ans)