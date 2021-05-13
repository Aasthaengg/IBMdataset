A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

min = min(a)+min(b)

for i in range(M):
    c =list(map(int,input().split()))
    s = a[c[0]-1]+b[c[1]-1]-c[2]
    min = (s if s < min else min)

print(min)