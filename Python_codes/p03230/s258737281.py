N = int(input())
flg = False
for i in range(N+1):
    if (i*(i+1))//2 == N:
        flg = True
        a = i
if flg == False:
    print('No')
    exit()
lis = [[0] * a for _ in range(a+1)]
p = 0
for i in range(a+1):
    for j in range(a):
        lis[i][j] = (i)*a+(j+1)-p
    p += (i+1)
#print(lis)
for i in range(1,a+1):
    for j in range(i):
        lis[i][j] = lis[j][i-1]
#print(lis)
print('Yes')
print(a+1)
for i in range(a+1):
    print(a,' '.join(map(str,lis[i])))




