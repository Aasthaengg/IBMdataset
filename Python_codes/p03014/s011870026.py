H,W = map(int,input().split())

S = [[] for _ in range(H)]
for i in range(H):
    S[i] = list(input())

HL = [[] for _ in range(H)]
WL = [[] for _ in range(W)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            HL[i].append(j)

for j in range(W):
    for i in range(H):
        if S[i][j] == '#':
            WL[j].append(i)
ma = 0
import bisect
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ind = bisect.bisect_left(HL[i],j)
            if ind == 0:
                left = -1
            else:
                left = HL[i][ind-1]
            if ind == len(HL[i]):
                right = W
            else:
                right = HL[i][ind]
            wid_num = right-left-1

            ind_2 = bisect.bisect_left(WL[j],i)
            if ind_2 == 0:
                up = -1
            else:
                up = WL[j][ind_2-1]
            if ind_2 == len(WL[j]):
                down = H
            else:
                down = WL[j][ind_2]
            len_num = down-up-1

            ma = max(ma,wid_num+len_num-1)
print(ma)






