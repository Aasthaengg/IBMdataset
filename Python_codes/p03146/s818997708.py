import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = inint()

a = [s]
al = [s]


for i in range(1, 1000001):
    if a[i-1] % 2 == 0:
        if a[i-1]//2 not in al:
            al.append(a[i-1]//2)
            a.append(a[i-1]//2)
        else:
            print(i+1)
            break
    else:
        if a[i-1]*3+1 not in al:
            al.append(a[i-1]*3+1)
            a.append(a[i-1]*3+1)
        else:
            print(i+1)
            break
