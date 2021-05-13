import bisect

n,q = list(map(int, input().split()))

list_xst = []
for _ in range(n):
    s,t,x = list(map(int, input().split()))
    list_xst.append([x, s-x, t-x])

list_xst.sort(key=lambda l:l[0])

list_d = [int(input()) for _ in range(q)]

retn = [-1] * q
jmp = [-1] * q

for x,s,t in list_xst:
    i = bisect.bisect_left(list_d, s)
    tt = bisect.bisect_left(list_d, t)
    while i < tt:
        if (jmp[i] != -1):
            i = jmp[i]
        else:
            retn[i] = x
            jmp[i] = tt
            i += 1

print(*retn, sep="\n")