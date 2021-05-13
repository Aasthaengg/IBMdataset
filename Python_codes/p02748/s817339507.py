A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
for i in range(M):
    xi = list(map(int, input().split()))
    c.append(a[xi[0]-1]+b[xi[1]-1]-xi[2])
print(min(min(a)+min(b), min(c)))
