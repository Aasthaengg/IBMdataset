import sys
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n = int(input())
import sys
vals = [None]*n
def quest(q):
    print(q)
    sys.stdout.flush()
    res = input()
    if res=="Vacant":
        exit()
        res = -1
    elif res=="Male":
        res = 1
    else:
        res = 0
    vals[q] = res
    return res

k = n//2
res1 = quest(0)
res2 = quest(k)

if (res2-res1)%2 != k%2:
    l = 0
    r = k
else:
    l = k
    r = n
    
while l<r+1:
    m = (l+r)//2
    res = quest(m)
    if (res-vals[l])%2 != (l-m)%2:
        r = m
    else:
        l = m
quest(l)
quest(r)