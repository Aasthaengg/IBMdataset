n = int(input())
Hs = list(map(int,input().split()))
f = [0 for _ in range(n)]
c = 0
r = 0
while r != n:
    r = 1
    for i in range(n):
        if f[i] < Hs[i] :
            if r > 0:
                c += 1
            r = 0
            f[i] += 1
        else:
            r += 1
    r -= 1   
print(c)