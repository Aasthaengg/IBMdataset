n = int(input())

sp = []
for i in range(1,n+1):
    s,p = input().split()
    sp.append([s,int(p),i])

sp.sort(reverse = True,key = lambda x:x[1])
sp.sort(key = lambda x:x[0])

for i in range(n):
    print(sp[i][2])