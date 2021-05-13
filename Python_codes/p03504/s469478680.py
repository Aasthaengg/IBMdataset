import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N,C = map(int,input().split())
time = [0]*(100009*2)
channel = [[0]*(100009*2) for _ in range(C)]
#(方針)チャンネル関係なしに
#同じチャンネルの連続だと録画開始時間に0.5秒のロスがない
# 同チャンネルで 1-7 7-8 → [0.5,8) → 録画機1つ(0.5~7.99) 
# 違うチャンネルで 1-7 7-8 → [0.5,7) 0.5~6.99 , [6.5,8) 6.5~7.99 → 録画機2つ

#前処理:　同チャンネル#0.5が扱いずらいので,sを2s-1,tを2tに対応させる
#ex: 1-3 → 0.5-3 → 1-6
#ex: 3-5 → 2.5-5 → 5-10
#ex: 1-3,3-5 → 1-6,5-10 → 2個必要の区間をつなげる(ex. 1-7 7-8 → 1-8）
max_num = 0
for i in range(N):
 s,t,c = map(int,input().split())
 s,t = 2*s-1,2*t 
 if(channel[c-1][s-1] == 1): channel[c-1][s-1] = 0
 else: channel[c-1][s] = 1
 channel[c-1][t] = 1
 max_num = max(max_num,t)

#imos法
#0.5が扱いずらいので,sを2s-1,tを2tに対応させる
#ex: 1-3 → 0.5-3 → 1-6
#ex: 3-5 → 2.5-5 → 5-10
#ex: 1-3,3-5 → 1-6,5-10 → 2個必要
#A = []
tmp = 0
for i in range(C):
 for j in range(max_num+10):
  if((tmp == 0)and(channel[i][j] == 1)):
    tmp = 1
    a = j
  elif((tmp == 1)and(channel[i][j] == 1)):
    tmp = 0
    b = j
    #A.append([a,b])
    time[a] += 1
    time[b+1] -= 1
#print(A)
    
ans = 0
for i in range(max_num+10):
  if(i != 0): time[i] += time[i-1]
  ans = max(ans,time[i])
print(ans)
#print(time)