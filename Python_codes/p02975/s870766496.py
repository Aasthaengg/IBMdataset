n = int(input())
A = list(map(int, input().split()))

def rule1(L):
    if len(set(L))!=2:
        return False
    if L.count(0)!=len(L)//3:
        return False
    return True

def rule2(L):
    if len(set(L))!=3:
        return False
    sL = set(L)
    if L.count(list(sL)[0])==L.count(list(sL)[1])==L.count(list(sL)[2]):
        if list(sL)[0] ^ list(sL)[1] ^ list(sL)[2] ==0:
            return True
        else:
            return False
    else:
        return False

if sum(A)==0 or rule1(A) or rule2(A):
    print('Yes')
else:
    print('No')
