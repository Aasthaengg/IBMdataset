N,M = map(int,input().split())

k=[]
s=[]

for i in range(M):
    switch = list(map(int,input().split()))
    k.append(switch[0])
    s.append(switch[1:])
    
p = list(map(int,input().split()))


count = 0
for i in range(2**N):
    lighton_num = 0
    for m in range(M):
        switchon_num = 0
        for j in range(k[m]):
            
            if (i>>(s[m][j]-1)) &1== 1:
                switchon_num+=1
            
        
        if switchon_num%2 == p[m]:
            lighton_num += 1
        # print(bin(i), m, j,switchon_num,p[m], lighton_num, count)
        
    if lighton_num == M:
        count += 1

print(count)