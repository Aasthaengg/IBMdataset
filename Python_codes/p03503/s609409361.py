N = int(input())
F=[]
for _ in range(N):
    F.append(int(''.join(input().split()), 2))
P=[]
for _ in range(N):
    P.append(list(map(int, input().split())))
#print(N)
#print(list(map(bin, F)))
#print(P)

profit_list=[]
for i in range(1, 2 ** 10):
    profit=0
    for k in range(N):
        kaburi = i & F[k]
        #print(bin(i), bin(F[k]), bin(kaburi))
        kaburi_count=0
        for j in range(10):
            if ((kaburi >> j) & 1):
                kaburi_count+=1
        profit+=P[k][kaburi_count]
    profit_list.append(profit)
#print(profit_list)
print(max(profit_list))
