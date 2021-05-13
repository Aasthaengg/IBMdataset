n,k = map(int, input().split())
w = [int(input()) for _ in range(n)]

def bs(left, right):
    mid = 0
    
    while left < right:
        mid = (left + right ) //2
        if check(mid, w, k):
            right = mid
        else:
            mid += 1
            left = mid
    return mid

def check(v, wgt, num):
    cnt = 1
    tmp = 0
    for j in wgt:
        tmp += j
        if tmp > v:
            tmp = j
            cnt += 1
            if cnt > num:
                return False
    return True
    
print(bs(max(w), sum(w)))