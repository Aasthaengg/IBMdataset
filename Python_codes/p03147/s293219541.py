n = int(input())
h = list(map(int,input().split()))
p = 0
while h.count(0) != n:
    x = 0
    for i in range(n):
        if h[i] == 0:
            if x != i:
                for j in range(x,i):
                    h[j] -= 1
                p += 1
                x = i + 1
            else:
                x += 1     
    if h[-1] != 0:
        for i in range(x,n):
            h[i] -= 1
        p += 1
print(p)