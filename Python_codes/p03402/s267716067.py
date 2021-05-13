import sys,collections as cl,bisect as bs,math
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
    return list(map(int,input().split()))
def m():
    return map(int,input().split())
def onem():
    return int(input())
def s(x):
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa == x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x):
    return " ".join(map(str,x))

a,b = m()

print(100,100)
aa = [["." for i in range(100)] for j in range(100)]
c = 0
for i in range(50):
    for j in range(100):
        aa[i][j] = "#"
a -= 1
b -= 1
k = 0
for i in range(100):
    if i <= 48:
        if k == 1:
            k = 0
            continue
        if a != 0:
            for j in range(100):
                if a == 0:
                    break
                if i//2 % 2 == 0:
                    if j % 2 == 0:
                        aa[i][j] = "."
                        a -= 1
                        k = 1
                else:
                    if j % 2 == 1:
                        aa[i][j] = "."
                        a -= 1
                        k = 1
    elif i >= 51:
        if k == 1:
            k = 0
            continue
        if b == 0:
            break
        else:
            for j in range(100):
                if b == 0:
                    break
                if i//2 % 2 == 0:
                    if j % 2 == 0:
                        aa[i][j] = "#"
                        b -= 1
                        k = 1
                else:
                    if j % 2 == 1:
                        aa[i][j] = "#"
                        b -= 1
                        k = 1
    else:
        k = 0

for i in range(100):
    print("".join(aa[i]))