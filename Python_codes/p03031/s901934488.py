#N = int(input())
n, m = map(int, input().split())
#hl = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(m)]
pl = list(map(int, input().split()))
count=0
for i in range(2**n):
    b = bin(i)
    switch = [False for i in range(n)]
    boollist=[]
    for j in range(n):
        if ((i >> j) & 1):
            switch[j] = True
    for j in range(m):
        k = l[j][0]
        sl = l[j][1:]
        total=0
        for sij in sl:
            if switch[sij-1]:
                total+=1
        if total % 2 == pl[j]:
            boollist.append(True)
        else:
            boollist.append(False)
    if all(boollist):
        count += 1
print(count)

