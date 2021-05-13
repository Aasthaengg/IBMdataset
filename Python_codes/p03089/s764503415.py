n = int(input())
x = list(map(int,input().split()))
x.reverse()
ans =[]
c=1
for i in range(n):
    c=0
    for j in range(n-i):
        if x[j]==n-i-j:
            ans.append(x.pop(j))
            c=1
            break
    if c==0:
        print('-1')
        exit()    
ans.reverse()
for i in ans:
        print(i)
