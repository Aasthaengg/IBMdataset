#coding:utf-8

import itertools

def goukei(b , x):
    count = 0
    for i in range(len(b)):
        if sum(b[i]) == x:
            count += 1
    return count

n =1
x =1

while n+x != 0:
    n , x = [int(i) for i in input().rstrip().split(" ")]

    if n + x == 0:
        break
    
    a = [i for i in range(1,n+1)]
#?????????????????????????????????
    kumi = list(itertools.combinations(a ,3))
    
    print(goukei(kumi,x))