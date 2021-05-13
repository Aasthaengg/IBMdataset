# 初期入力
import sys
input = sys.stdin.readline
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

count =[0]*N
if N ==1:
    count[0] =A1[0] +A2[0]
else:
    for i in range(N-1):
        count[i] =sum(A1[:i+1]) +sum(A2[i:])
print(max(count))