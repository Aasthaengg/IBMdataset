n = int(input())
dat = [None] * n

def su(x):
    print(x)
    r = input()
    if r == "Vacant":
        return True
    elif r == "Male":
        dat[x] = "M"
        return False
    elif r == "Female":
        dat[x] = "F"
        return False
def do():
    if su(0):
        return 0
    if su(n-1):
        return 0
    l = 0
    r = n-1
    while True:
        mid = (l+r) // 2
        if su(mid):
            return 0

        if (mid - l) % 2 == 1: #even個
            if dat[l] == dat[mid]: # ここが変
                r = mid
                continue
        else: # odd
            if dat[l] != dat[mid]: # koko
                r = mid
                continue

        if (r - mid) % 2 == 1: #even個
            if dat[r] == dat[mid]: # ここが変
                l = mid
                continue
        else: # odd
            if dat[r] != dat[mid]: # koko
                l = mid
                continue
do()
