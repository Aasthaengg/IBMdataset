N = int(input())
A = list(map(int, input().split()))

A.sort()

def check(sz):
    # print("check:", sz)
    skp = False
    cannot_eat = False
    check = sz
    for i in A:
        if skp == False and sz == i:
            skp = True
            continue

        if i > check * 2:
            cannot_eat = True
            break
        else:
            check += i
    # print("result:", cannot_eat)
    return not cannot_eat

ok = N
ng = -1


while abs(ok-ng)>1:
    mid = (ok+ng)//2

    if check(A[mid]):
        # ok
        ok = mid
    else:
        # ng
        ng = mid
    
    # print(ok, ng)

print(N-ok)