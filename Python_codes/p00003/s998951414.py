n = int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    idx = l.index(max(l))
    c = l[idx]
    a, b  = [x for i,x in enumerate(l) if i != idx] 
    if a**2 + b**2 == c**2:
        print("YES")
    else:
        print("NO")