#2問目
#ナップザック問題
N = int(input())
S = []
count = 0
for i in range(N):
    s = int(input())
    S.append(s)
S.sort()
#最大値はlistの中をすべて足し合わせた数
DP = [0] * (sum(S) + 1)
DP[0] += 1
for i in S:
    #選ぶ時
    for j in range(len(DP)-1, -1, -1):
        if DP[j] != 0:
            DP[i+j] = 1

flag = False

for i in range(len(DP)-1, -1, -1):
    if(DP[i] != 0 and i % 10 != 0 and flag == False):
        print(i)
        flag = True
        
if flag != True:
    print(0)