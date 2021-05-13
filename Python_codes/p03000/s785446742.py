# 初期入力
import sys
input = sys.stdin.readline
N,X = (int(x) for x in input().split())
L = list(map(int, input().split()))
d =[0]*(N+1)
count =1
for i in range(N):
    d[i+1] =d[i] +L[i]
    if d[i+1] <= X:
        count +=1
    else:
        break
print(count)