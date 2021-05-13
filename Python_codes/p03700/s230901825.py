import sys
I = lambda:int(sys.stdin.readline())
LI = lambda:[int(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for _ in range(n)]

N,A,B = LI()
H = IR(N)

def isOK(c):
    cnt = 0
    for enc in H:
        if enc - B*c > 0:
            cnt += ((enc - B*c)+(A-B)-1)//(A-B)
            if cnt > c:
                return False
    return True

OK = (max(H)+B-1)//B
NG = 0

while(OK-NG>1):
    mid = (OK+NG)//2
    if isOK(mid):
        OK = mid
    else:
        NG = mid

print(OK)


