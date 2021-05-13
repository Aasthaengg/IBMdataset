N = int(input())
a = list(map(int, input().split()))
b = []
c = []
for i in range(N):
    if i<N//2:
        b.append(-1)
    else:
        b.append(a[i])

for i in reversed(range(N//2)):
    t = 1
    s = 0
    while (i+1)*(t+1)<=N:
        s+=b[(i+1)*(t+1)-1]
        t+=1
    if s%2 != a[i]:
        b[i]=1
    else:
        b[i]= 0
#print(b)

bo = False
for j in range(N):
    if b[j]==1:
        bo = True
        c.append(str(j+1))
if bo:
    print(len(c))
    print(" ".join(c))
else:
    print(0)