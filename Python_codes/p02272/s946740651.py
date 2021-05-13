def f():
    return int(raw_input())
def f2():
    return map(int, raw_input().split())

def merge(left, mid, right):
    L = S[left:mid]
    R = S[mid:right]
    lp, rp, xp = 0, 0, 0
    a, b = L[0], R[0]
    c = right - left
    x = [0] * c
    while xp < c:
        while xp < c and a <= b:
            x[xp] = a
            lp += 1
            xp += 1
            try:
                a = L[lp]
            except:
#                print x[xp:c], R[rp:right-mid]
                for e in R[rp:]:
                    x[xp] = e
                    xp += 1
                    rp += 1
                break
        while xp < c and a >= b:
            x[xp] = b
            rp += 1
            xp += 1
            try:
                b = R[rp]
            except:
#                print x[xp:c], L[lp:mid-left]
                for e in L[lp:]:
                    x[xp] = e
                    xp += 1
                    lp += 1
                break
    S[left:right] = x
    return c

def mergesort(left, right):
    c = 0
    if left + 1 < right:
        mid = (left + right)/2
        c += mergesort(left, mid)
        c += mergesort(mid, right)
        c += merge(left, mid, right)
    return c

global S
n = f()
S = f2()

c = mergesort(0, n)
print " ".join(map(str,S))
print c