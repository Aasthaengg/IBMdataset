N = int(input())
c = list(input())
cd = c[::-1]

rs = [0]*(N+1)
ws = [0]*(N+1)
ws[0]= 0
rs[0] = 0

for i in range(N):
    if(c[i]=="W"):
        rs[i+1]=rs[i]+1
    else:
        rs[i+1]=rs[i]

    if(cd[i]=="R"):
        ws[i+1]=ws[i]+1
    else:
        ws[i+1]=ws[i]
    
ws.reverse()

m = 1000000000
for i in range(N+1):
    M = max(rs[i],ws[i])
    if m>M:
        m = M
    
print(m)
