N = int(input())
a = list(map(int,input().split()))

mx = max(a)
mn = min(a)

proc = []
if mx >= (-1) * mn:
    i = a.index(mx)
    for j in range(len(a)):
        if a[j] < 0:
            proc.append([i+1,j+1])
            a[j] += a[i]

    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            proc.append([j+1,j+2])
            a[j+1] += a[j]

else:
    
    i = a.index(mn)
    for j in range(len(a)):
        if a[j] > 0:
            proc.append([i+1,j+1])
            a[j] += a[i]

    for j in reversed(range(len(a)-1)):
        if a[j] > a[j+1]:
            proc.append([j+2,j+1])
            a[j] += a[j+1]



print(len(proc))
for k in proc:
    print(k[0], k[1])
