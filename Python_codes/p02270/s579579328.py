# coding: utf-8
# Here your code !
n,k=map(int,input().split())

weight=[int(input()) for i in range(n)]
def binary_search(start,end):
    left = start
    right = end
    middle = 0
    while left < right:
        middle = (left + right)//2
        if simulate(middle,weight,k):
            right = middle
        else:
            left = middle + 1
    return left
 
def simulate(prb,wei,num):
    count = 1
    tmp = 0
    for j in wei:
        tmp += j
        if tmp > prb:
            tmp = j
            count += 1
            if count > num:
                return False
    return True
 
print(binary_search(max(weight), sum(weight)))