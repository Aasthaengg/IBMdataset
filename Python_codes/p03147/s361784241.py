# 初期入力
import sys
input = sys.stdin.readline
N = int(input())
h_aft = list(map(int, input().split()))
h_bef =[0]*N

#
count =0
while sum(h_bef) < sum(h_aft):
    flag =[0]*(N+1)
    for i in range(N):
        if h_bef[i] <h_aft[i]:
            h_bef[i] +=1
            flag[i] =1
    for i in range(N+1):
        if flag[i] ==1 and flag[i+1] ==0:
            count +=1

print(count)