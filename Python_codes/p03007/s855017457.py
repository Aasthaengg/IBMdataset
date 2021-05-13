import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
pos, neg, zero = [], [], []

for Ai in A:
    if Ai>0:
        pos.append(Ai)
    elif Ai<0:
        neg.append(Ai)
    else:
        zero.append(0)

if len(neg)==0:
    neg += zero
else:
    pos += zero
    
ope = []

if len(pos)>0 and len(neg)>0:
    now1 = pos[0]
    
    for i in range(1, len(neg)):
        ope.append((now1, neg[i]))
        now1 -= neg[i]
    
    now2 = neg[0]
    
    for i in range(1, len(pos)):
        ope.append((now2, pos[i]))
        now2 -= pos[i]
    
    ope.append((now1, now2))
    M = now1-now2
elif len(pos)==0:
    neg.sort(reverse=True)
    now = neg[0]
    
    for i in range(1, len(neg)):
        ope.append((now, neg[i]))
        now -= neg[i]
    
    M = now
else:
    pos.sort()
    now = pos[0]
    
    for i in range(1, len(pos)-1):
        ope.append((now, pos[i]))
        now -= pos[i]
    
    ope.append((pos[-1], now))
    M = pos[-1]-now

print(M)

for x, y in ope:
    print(x, y)