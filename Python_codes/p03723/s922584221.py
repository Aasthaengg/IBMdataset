def IsOdd(n):
    if n % 2 == 0:
        return True
    else:
        return False

A,B,C = map(int,input().split())

cnt = 0
inf = False
while True:
    if IsOdd(A) and IsOdd(B) and IsOdd(C):
        if A == B == C:
            inf = True
            break
        else:
            a,b,c = A//2,B//2,C//2
            A,B,C = b+c,c+a,a+b
            cnt += 1
    else:
        break
if inf:
    print(-1)
else:
    print(cnt)