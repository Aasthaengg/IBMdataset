import math, sys

def loadable(w, n, k, p, wsum):
    wait = 0
    for i in range(n):
        wait += w[i]
        wsum -= w[i]
        if wait > p:
            k -= 1
            wait = w[i]
            if k == 0 or p < wsum / k:
                return False
    return True

n, k = map(int, sys.stdin.readline().split())
w = [int(sys.stdin.readline()) for _ in range(n)]

wsum = sum(w)

p = max(int(math.ceil(wsum / k)), max(w))
pre_f = p -1
pre_s = None

while True:
    if loadable(w, n, k, p, wsum):
        pre_s = p
    else:
        pre_f = p

    if pre_s != None and pre_s - pre_f == 1:
            break
    
    if pre_s:
        p = int((pre_s + pre_f) / 2)
    else:
        p = math.ceil(p * 1.01)
    
print(pre_s)