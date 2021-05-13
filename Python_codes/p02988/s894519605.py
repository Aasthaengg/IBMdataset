# 初期入力
import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))

#
count =[]
for i in range(1,n-1):
    p3 =p[i-1:i+2]
    p3.sort()
    if p3[1] ==p[i]:
        count.append(i)
print(len(count))