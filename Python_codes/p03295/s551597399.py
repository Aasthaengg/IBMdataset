#この方法だとTLEになるためNG

from pprint import pprint
from copy import deepcopy

#N <= 10**5なので、全探索はNG
#Greedyでいける？


n,m = map(int,input().split())

requests = [list(map(int,input().split())) for _ in range(m)]

#区間スケジュール問題と考え、終端が小さい順で並べる。その後Greedyで計算。
requests = sorted(requests, key=lambda x:x[1])

counter = 0
before_point = -float('inf')

#pprint(requests)

for i in range(m):
    if requests[i][0] >= before_point:
        counter += 1
        before_point = requests[i][1]
        #print("requests[{}]={} YES".format(i,requests[i]))
    else:
        #print("requests[{}]={} NO".format(i,requests[i]))
        pass

print(counter)
