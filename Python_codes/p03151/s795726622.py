n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b): print(-1)
else:
    cnt = 0
    Abs = []
    s = 0
    for i in range(n):
        if a[i] < b[i]: 
            cnt += 1
            s += b[i]-a[i]
        elif a[i] > b[i]:
            Abs.append(a[i]-b[i])
    Abs.sort(reverse=True)
    s2 = 0
    i = 0
    while s2 < s:
        s2 += Abs[i]
        i += 1
    print(i+cnt)