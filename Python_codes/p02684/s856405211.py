b,k = map(int,input().split())
a = list(map(int,input().split()))

i = 0
check = [True]*b
his = []
n = 0
his.append(0)
while(1):
    #print(his)
    i = a[i] - 1
    if check[i]:
        check[i] = False
        his.append(i)
    else:
        n = len(his)-his.index(i)
        break
m = len(his) - n
p = 0
if k > m:
    p = (k-m)%n + m
else:
    p = k
i = 0
#print(n,m,p)
for j in range(p):
    #print(a[i])
    i = a[i] - 1
print(i+1)

