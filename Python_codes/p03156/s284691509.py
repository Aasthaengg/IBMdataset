n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
l = []
m = []
h = []
for i in p:
    if i <= a:
        l.append(i)
    elif i <= b:
        m.append(i)
    else:
        h.append(i)
ans = min(len(l),len(m),len(h))
print(ans)

    
