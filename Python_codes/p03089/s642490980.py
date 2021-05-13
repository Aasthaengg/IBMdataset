n = int(input())
b = list(map(int, input().split()))
a = []
while b:
    m = len(b)
    ok = False
    for i in range(m)[::-1]:
        # print(m, i)
        if b[i] == i+1:
            a.append(b.pop(b[i]-1))
            ok = True
            break
    
    if not ok:
        print(-1)
        exit()

for i in range(n)[::-1]:
    print(a[i])