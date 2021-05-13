def resolve():
    H = int(input())
    cnt = 0
    mons = 1
    while H != 1:
        H = H//2
        cnt += mons
        mons *= 2
    print(cnt+mons)
    
if '__main__' == __name__:
    resolve()
