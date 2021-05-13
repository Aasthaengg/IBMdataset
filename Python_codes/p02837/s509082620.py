n= int(input())
test = [[]for _ in range(n)]
for i in range(n):
    num = int(input())
    for j in range(num):
     a, b= map(int,input().split())
     test[i].append([a-1,b])
ans = 0
for i in range(1,2**n):
    flag = 0
    for j in range(n):
        if(i>>j)&1 == 1:
            for x,y in test[j]:
                if(i>>x)&1 !=y:
                    flag = 1
                    break
    if flag == 0:
        ans = max(ans,bin(i)[2:].count('1'))
print(ans)

