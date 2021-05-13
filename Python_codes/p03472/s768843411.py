n,h = map(int,input().split())
A = []
B = []
m = 0
for j in range(n):
    a,b = map(int,input().split())
    m = max(a,m)
    A.append(a)
    B.append(b)
B.sort(reverse=True)
for i in range(n):
    if B[i] > m:
        h -= B[i]
    else:
        print(i+1+(h-1)//m)
        break
    if h <= 0:
        print(i+1)
        break
else:
    print(n+1+(h-1)//m)