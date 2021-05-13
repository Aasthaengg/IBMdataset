import sys
n,k = map(int,input().split())
w = list(map(int,sys.stdin.readlines()))

def binarysearch(start,end):
    left = start
    right = end
    middle = 0
    while left < right:
        middle = (left + right)//2
        if simulate(middle,w,k):
            right = middle
        else:
            left = middle + 1
    return left

def simulate(prb,wei,dai):
    count = 1
    tmp = 0
    for j in wei:
        tmp += j
        if tmp > prb:
            tmp = j
            count += 1
            if count > dai:
                return False
    return True

print(binarysearch(max(w), sum(w)))