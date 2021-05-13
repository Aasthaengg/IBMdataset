n, k = map(int, input().split())
a = list(map(int, input().split()))
b = a[::-1]
ans = 0
for i in range(1,min(n+1, k+1)):
    for j in range(i+1):
        m = i - j
        l = a[:m] + b[:j]
        ml = sorted([i for i in l if i < 0])
        pl = [i for i in l if i >= 0]
        ml = ml[min(k-i, len(ml)):]
        if ml:
            minus = sum(ml)
        else:
            minus = 0
        if pl:
            plus = sum(pl)
        else:
            plus = 0
        ans = max(ans, minus + plus)        
print(ans)