n = int(input())
r = 55555
sosu = [1] * (r+1)
sosu[0],sosu[1] = 0,0
sosu[2] = 1
for i in range(2,int(r**0.5)+3):
    for j in range(i*2,r+1,i):
        sosu[j] = 0

a = []
for i in range(r+1):
    if sosu[i] == 1:
        if i%5 == 1:
            a.append(i)
            
ans = []
for i in range(n):
    ans.append(a[i])
    
print(*ans)