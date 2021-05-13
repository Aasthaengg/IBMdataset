from collections import defaultdict
N,T = map(int,input().split())
a_ls = list(map(int,input().split()))
# 初期のa_lsにおける高橋くんのりんご一個あたりの最大利益を求める
Min = float('inf')
max_profit = 0
for i in range(N):
    if a_ls[i] < Min:
        Min = a_ls[i]
    else:
        max_profit = max(max_profit,a_ls[i]-Min)

#print(max_profit)

pair_dict = defaultdict(int)
Min = float('inf')
num_Min = 0
num_Max = 0
for i in range(N):
    #print(Min)
    #print(a_ls[i])
    #print('---')
    if a_ls[i] < Min:
        if num_Max > 0:
            pair_dict[(Min,Min+max_profit)] = min(num_Max,num_Min)
        Min = a_ls[i]
        num_Min = 1
        num_Max = 0
    elif a_ls[i] == Min:
        num_Min += 1
    elif a_ls[i] - Min == max_profit:
        num_Max += 1

if num_Max > 0:
    pair_dict[(Min,Min+max_profit)] = min(num_Max,num_Min)

ans = 0
#print(pair_dict)
for v in pair_dict.values():
    ans += v
print(ans)
