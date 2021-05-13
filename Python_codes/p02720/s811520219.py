k = int(input())
L = []

def lunlun(d,v,L):
    L.append(v)
    if d == 10:
        return
    for i in range(-1,2):
        t = v%10 + i
        #print(v)
        if 0 <= t <=9:
            lunlun(d+1,v*10+t,L)
#lunlun(1,1,L)
for v in range(1,10):
    lunlun(1,v,L)
print(sorted(L)[k-1])