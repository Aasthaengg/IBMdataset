n = int(input())
ex = [False]*(n+1)
ex[1] = True
for i in range(2, n+1):
    v = i*i
    if v>n: break
    while(v<=n):
        ex[v]=True
        v*=i
for i in range(1, n+1)[::-1]:
    if ex[i]:
        print(i)
        break