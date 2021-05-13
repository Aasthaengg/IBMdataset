import math
N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]


def enough(T):
    temp = 0
    ch = H[:]
    for h in ch:
        left = h - B*T
        if left > 0:
            temp += (left + A-B-1)//(A-B)
            #temp += math.ceil(left/(A-B))
            #print(temp)

    if temp > T:
        return False
    else:
        return True

#print(enough(2))
ok = 10**15
ng = 0

while ok - ng > 1:
    mid = (ok + ng)//2
    if enough(mid):
        ok = mid
    else:
        ng = mid
    #print(ok,ng)
print(ok)