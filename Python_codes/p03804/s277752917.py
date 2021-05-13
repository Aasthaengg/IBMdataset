n,m = map(int,input().split())
a = []
b = []
for i in range(n):
    tmp = input()
    a.append(tmp)
    
for i in range(m):
    tmp = input()
    b.append(tmp)
    
ans = False
for w in range(0 , n-m+1):
    for h in range(0,n-m+1):
        if ans == True:
            break
        flag = True
        for i in range(m):
            if a[h+i][w:w+m] == b[i]:
                pass
            else:
                flag = False
                break
        if flag == True:
            ans = True
if ans:
    print('Yes')
else:
    print('No')