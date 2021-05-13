a = int(input())
b = int(input())
c = int(input())
x = int(input())


ans = 0
for i in range(a+1):
    gh = 500*i
    for j in range(b+1):
        hy = 100*j
        for k in range(c+1):
            gj = 50*k
            t = gh + hy + gj
            if t == x:
                ans += 1

print(ans)
