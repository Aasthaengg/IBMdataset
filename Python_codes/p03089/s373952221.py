n = int(input())
b = list(map(int,input().split()))
p = []

for i in range(n):
    nn = len(b)
    for j in range(nn-1,-1,-1):
        if b[j] == j+1:
            p.append(b[j])
            b = b[:j]+b[j+1:]
            break
            
if b == []:
    for i in range(n-1,-1,-1):
        print(p[i])
else:
    print(-1)