import math as ma
# import statistics as stat
while True:
    n = int(input())

    if (n == 0):
        break

    score = list(map(int,input().split()))
    m = sum(score)/len(score)
    tmp = [0]*len(score)
    for i in range(len(score)):
        tmp[i] = float((score[i]-m)**2)

    s = sum(tmp)
    div =ma.sqrt(s/len(score))
    print(div)

