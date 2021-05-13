n,m = map(int,input().split())
xyz = [[int(i) for i in input().split()] for j in range(n)]

ans = 0

num = 2**3

for i in range(num):
    tmp = format(i,'0'+str(3)+'b')
    li = []
    for j in range(n):
        kari = 0
        for k in range(3):
            kari += xyz[j][k]*(-1)**int(tmp[k])
        li.append(kari)
    li.sort(reverse=True)
    temp = 0
    for l in range(m):
        temp += li[l]
    ans = max(ans,temp)
    
print(ans)