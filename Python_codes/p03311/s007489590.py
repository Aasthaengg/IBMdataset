N = int(input())
a = list(map(int, input().split()))

aa = [ai - i-1 for i,ai in enumerate(a)]

def tri_search(f:"f(x:float)->float", left, right, iter=100)->float:
    for _ in range(iter):
        ml = (left*2 + right) / 3
        mr = (left + right*2) / 3
        if f(ml) < f(mr):
            right = mr
        else:
            left = ml
    # print(left, right)
    return (right + left) / 2

def f(x):
    ret = 0
    x = int(x+0.5)
    for aai in aa:
        ret += abs(aai - x)
    return ret

b = tri_search(f, -10**9, 10**9)
print(min(f(b), f(b+1), f(b-1)))
