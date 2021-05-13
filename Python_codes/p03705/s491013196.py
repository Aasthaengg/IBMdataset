N,A,B=map(int, input().split())
#最小がA　最大がB　その区間でN個
if A>B:
    print(0)
    exit()
elif N==1 and A!=B:
    print(0)
    exit()
MAX=A+B*(N-1)
MIN=B+A*(N-1)
#print(MAX, MIN)
print(MAX-MIN+1)