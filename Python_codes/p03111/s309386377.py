# C - Synthetic Kadomatsu
'''
100, 90, 80
98, 80, 40, 30, 21
L[0]〜L[N-1]がそれぞれ、A,B,C,使わないのいずれかかを考える。
4**8=65536
'''
import itertools
INF = 10**18
N, A, B, C = map(int, input().split())
L = [0] * N
for i in range(N):
    L[i] = int(input())
    
c = (0, 1, 2, 3) # 3は使わない
ans = INF

for comb in itertools.product(c,repeat=N):
    tmp = [0]*4 
    ansArr = [0]*3
    #print(comb)
    for i, j in enumerate(comb):
        if tmp[j]==0:
            tmp[j] += L[i]
        elif j!=3:
            tmp[j] += L[i]
            ansArr[j] += 10
    if tmp[0]==0 or tmp[1]==0 or tmp[2]==0:
        continue
    ansArr[0] += abs(A-tmp[0])
    ansArr[1] += abs(B-tmp[1])        
    ansArr[2] += abs(C-tmp[2])
    #print(tmp)
    #print(ansArr)
    ans = min(ans, sum(ansArr))
    #print(ans)

print(ans)