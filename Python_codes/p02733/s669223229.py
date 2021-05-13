from itertools import *
H, W, K = map(int, input().split())
S = [list(map(int, input())) for i in range(H)]
ans = 100000
for p in product([0,1],repeat=H-1):
    tmp_ans = sum(p)
    index = []
    for i,j in enumerate(p):
        if j == 1:
            index.append(i+1)
    count = [0] * (len(index) +1)
    for w in range(W):
        plate = [yoko[w] for yoko in S]
        tmp = [0]*(len(index)+1)
        if index == []:
            tmp[0] = sum(plate)
        else:
            tmp[0] = sum(plate[0:index[0]])
            for itr in range(len(index)):
                if itr == len(index) -1:
                    tmp[itr+1] += sum(plate[index[itr]:])
                else:
                    tmp[itr+1] += sum(plate[index[itr]:index[itr+1]])
        if max(tmp) > K :
            tmp_ans = 11111111111
        tmp_sum = [x+y for (x,y) in zip(count,tmp)]
        if max(tmp_sum) > K:
            tmp_ans +=1
            count = tmp
        else:
            count = tmp_sum
    if tmp_ans < ans:
        ans = tmp_ans

print(ans)





