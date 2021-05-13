r,g,b,n = map(int,input().split())
p = 0
for i in range(n+1):
    ri = r*i
    if ri > n:
        break
    else:
        for j in range((n+1)-(r*i)):
            gj = g*j
            if ri + gj > n:
                break
            else:
                if (n - (ri + gj)) % b == 0:
                    p += 1
print(p)