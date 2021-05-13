
[N,Q] = list(map(int,input().split()))
S = input()

lr = []
for i in range(Q):
    lr.append(list(map(int,input().split())))

#C:1(左がAの場合)
flag=[0]*N
for i in range(1,N):
    if S[i]=='C' and S[i-1]=='A':
        flag[i]=1

#t = 1からiまでのAC出現回数
t=[0]
for i in range(1,N):
    t.append(t[-1] + flag[i])
# print('flag, t:', flag, t)

#Qに答えていく
for i in range(Q):
    print(t[lr[i][1]-1] - t[lr[i][0]-1])
