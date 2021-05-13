n,k = map(int,input().split())
A = list(map(int,input().split()))
ng = 0
ok = max(A)

def queri(n):
    count = 0
    for i in A:
        count += -(-i//n)-1
    if k>= count:
        return True
    else:
        return False

while ok - ng > 1:
    mid = (ok+ng)//2
    if queri(mid) :
        ok = mid
    else:
        ng = mid
print(ok)