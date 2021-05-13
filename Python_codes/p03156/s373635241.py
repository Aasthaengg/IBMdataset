n = int(input())
a,b = map(int,input().split())
L = list(map(int,input().split()))

p,q,r = [],[],[]
for i in range(n):
    if 0<=L[i]<=a:
        p.append(L[i])
    elif a+1 <= L[i] <=b:
        q.append(L[i])
    else:
        r.append(L[i])
print(min(len(p),len(q),len(r)))