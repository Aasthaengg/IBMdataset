nn = int(input())
aa = list(map(int,input().split()))
#print(aa)
aa.sort()
#print(aa)

flag = 0

for i in range(nn-1):
    if (aa[i] == aa[i+1]) and (flag == 0):
        print('NO')
        flag = 1

if flag == 0:
    print('YES')