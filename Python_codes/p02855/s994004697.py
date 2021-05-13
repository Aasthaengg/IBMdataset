[H,W,K] = list(map(int,input().split()))

s = []
for i in range(H):
    s.append(list(input()))
# print('s:',s)

##１行に何個いちごあるか
ichigo=[]
nai=[]  #苺がない行
flg=0
for i in range(H):
    dammy=0
    for j in range(W):
        if s[i][j] =='#':
            if flg==0:
                X = i
                flg=1
            dammy += 1
    if dammy==0:
        nai.append(i)
    ichigo.append(dammy)
# print('ihigo,nai:',ichigo,nai)

out = [[0]*W for i in range(H)] #2次元配列はこう準備(値わたし)、[[0
cnt=0
lim=0
for i in range(H):
    if i in nai:
        continue
    else:
        cnt+=1
        lim+=ichigo[i]
        for j in range(W):
            out[i][j]=cnt
            if s[i][j] =='#' and cnt!=lim:
                cnt+=1
            # print('lim,cnt:',lim,cnt)


for i in nai:
    if i<X:
        out[i] = out[X]
    else:
        # if i==0:
        #     out[0] = out[1]
        # else:
        out[i] = out[i-1]

for i in range(H):
    print(*out[i])