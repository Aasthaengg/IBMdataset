a,b,q = map(int,input().split())

sl = [-float("inf")]
for _ in range(a):
    sl.append(int(input()))
sl.append(float("inf"))
tl = [-float("inf")]
for _ in range(b):
    tl.append(int(input()))
tl.append(float("inf"))
    
import bisect


for _ in range(q):
    x = int(input())
    index1 = bisect.bisect(sl, x) 
    index2 = bisect.bisect(tl, x)
    rs = abs(sl[index1] - x) 
    ls = abs(sl[index1-1] - x)
    rt = abs(tl[index2] - x)
    lt = abs(tl[index2-1] - x)
    ansl = []
    ansl.append(max(rs,rt))
    ansl.append(max(ls,lt))
    ansl.append(2*min(rs,lt)+max(rs,lt))
    ansl.append(2*min(ls,rt)+max(ls,rt))
    print(min(ansl))
    
