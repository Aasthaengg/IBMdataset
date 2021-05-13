n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))

"""
def dec2bin(n):
    amari = [[] for j in range(2**n)]
    for i in range(2**n):
        while i != 0:
            amari[i].append(i%2)
            i = i // 2
        if len(amari[i]) != n:
            while len(amari[i]) < n:
                amari[i].append(0)
        amari[i].reverse()
    return amari
"""
def dec2bin(target):
    amari = []
    while target != 0:
        amari.append(target % 2)
        target = target //2
    if len(amari)!=n:
        while len(amari)<n:
            amari.append(0)
    amari.reverse()
    return amari

b = [[] for i in range(2**n)]
for j in range(2**n):
    b[j] = dec2bin(j)


vc = 0
for i in range(2**n):
    vsum = 0
    csum = 0
    for j in range(n):
        if b[i][j] == 1:
            vsum += v[j]
            csum += c[j]
    if vc <= vsum - csum:
        vc = vsum - csum
print(vc)