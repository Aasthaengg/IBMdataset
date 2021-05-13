n = int(input())
a = list(int(input()) for i in range(n))
t = []
o = 1

while o != 2:
    if len(t) > n:
        print(-1)
        exit(0)
    t.append(o)
    o = a[o-1]

print(len(t))