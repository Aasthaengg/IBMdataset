# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 00:26:07 2020

@author: liang
"""

"""
コーナーケース１:
    重複があるとき　not coprime(※これが誤り)
    ただし、1の重複は除く

コーナーケース:
    重複があるとき　pairwise coprime ではない
    setwise coprimeの可能性はある
    ただし、１の重複は
"""
import math
C = 10**6
#T = int(math.sqrt(C)*10**3)+1
N = int(input())
judge = [0]+[False]*C
A =list()
f = True
for a in input().split():
    if judge[int(a)] == True and int(a) != 1:
        f = False
    judge[int(a)]=True
    A.append(int(a))
d = [False]+[True]*C

#print(judge[:10])
def solve(f):
    flag = True
    #エラトステネスの篩 O(N log N)
    for i in range(2,C+1):
        count = 0
        if d[i] == True:
            for j in range(i,C+1,i):
                if judge[j] == True:
                    count += 1
                if count == 2:
                    flag = False
                    break
                d[j] = False
        if not flag:
            break
    
    if flag == True and f == True:
        return "pairwise coprime"
    ans = A[0]
    #線形探索 O(N)
    for i in range(N):
        ans = math.gcd(ans,A[i])
    #print("ans",a)
    if ans == 1:
        return "setwise coprime"
    return "not coprime"

print(solve(f))
#print(len(A))