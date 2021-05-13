import sys,math,collections,itertools,copy
input = sys.stdin.readline

D,G=list(map(int,input().split()))
score = []
maxScore = []
cos_per = []
maxS = []
for d in range(D):
    p,c=map(int,input().split())
    tmp = [(d+1)*100]*p
    tmp[-1]+=c
    score.append(tmp)
    maxScore.append(sum(tmp))
    maxS.append([p,sum(tmp)])
    #cos_per.append([d+1,sum(tmp)/p])
    cos_per.append([d+1,d+1])
#-最大いくつの問題セットを必要とするか-#
maxScore.sort()
tmp = 0
for idx,mS in enumerate(maxScore):
    tmp += mS
    if tmp >= G:
        max_num = idx+1
        break
#-最小でいくつの問題セットを必要とするか-#
tmp = 0
j=0
for i in range(len(maxScore)-1,-1,-1):
    j+=1
    tmp += maxScore[i]
    if tmp >= G:
        min_num = j
        break
#-最小-2個はスコアが高いものを入れてよし-#
#cos_per.sort(key = lambda x:-x[1])
choice = set(range(1,D+1))
#choiceList = []
#for i in range(0,min_num-3):
 #   choiceList+=score[cos_per[i][0]-1]
 #   choice.discard(cos_per[i][0])
 #   max_num -=1
 
#-足し上げる-#

ans = float('inf')
for ch in itertools.permutations(choice,max_num):
    times = 0
    total = 0
    flag = 0
    for ci in ch:
        if total + maxS[ci-1][1] <G:
            total += maxS[ci-1][1]
            times += maxS[ci-1][0]
        else:
            for sc in score[ci-1]:
                total += sc
                times += 1
                if total >= G:
                    ans = min(ans,times)
                    falg = 1
                    break
    if flag ==1:
        break
print(ans)     
