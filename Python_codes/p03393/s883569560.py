a = list(input())
ar = list('abcdefghijklmnopqrstuvwxyz')
if len(a) < 26:
    for r in ar:
        if r not in a:
            print("".join(a) + r)
            exit()
else:
    for i in range(25,0,-1):
        n = ar.index(a[i-1]) 
        b = [ar.index(a[j]) for j in range(i,26)]
        br = []
        for r in b:
            if r > n:
                br.append(r)
        if len(br) > 0:
            print("".join(a[0:i-1]) + ar[min(br)])
            exit()
print(-1)