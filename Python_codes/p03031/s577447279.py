n, m = (int(xi) for xi in input().split())
k = []
for xi in range(m):
    ksub = [int(xi) for xi in input().split()]
    k.append(ksub[1:])
p = [int(xi) for xi in input().split()]

# print(k)


countN = 0
for Nnum in range(2**n):
    txt = bin(Nnum)[2:]
    txt = "0"*(n-len(txt))+txt
    # print(txt)

    for li in range(m):
        ltxt = "0"*n
        for xi in range(len(k[li])):
            point = k[li][xi]-1
            ltxt = ltxt[:point]+"1"+ltxt[point+1:]
        # print(ltxt)
        count = 0
        for xi in range(n):
            if txt[xi]=="1" and ltxt[xi]=="1":
                count += 1
        if count%2==p[li]:
            switch = True
        else:
            switch = False
            break
    if switch: countN += 1

print(countN)
