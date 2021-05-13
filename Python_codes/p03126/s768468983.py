# 初期入力
import sys
input = sys.stdin.readline
N,M = (int(i) for i in input().split())
K =[0]*N
A=[]
for i in range(N):
    a,*b = list(map(int, input().split()))
    K[i] =a
    A.append(set(b))
ans =set(list(A[0]))
for i in A:
    ans &=i
print(len(ans))