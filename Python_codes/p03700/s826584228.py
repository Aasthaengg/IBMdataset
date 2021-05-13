import sys
I = lambda:int(sys.stdin.readline())
LI = lambda:[int(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for _ in range(n)]

def check(a,b,h,c):
    cnt = 0
    for enc in h:
        if enc - b*c > 0:
            cnt += ((enc - b*c)+(a-b)-1)//(a-b)
            if cnt > c:
                return False
    return True


N,A,B = LI()
H = IR(N)

OK = (max(H)+B-1)//B
NG = 0

while(OK-NG>1):
    mid = (OK+NG)//2
    if check(A,B,H,mid):
        OK = mid
    else:
        NG = mid

print(OK)


