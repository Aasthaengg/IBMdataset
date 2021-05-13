# 初期入力
import sys
input = sys.stdin.readline
A = list(map(int, input().split()))

a =max(A)
coin =a
a -=1
A.append(a)

A.sort()
a_2 =A[1]
coin +=a_2

print(coin)