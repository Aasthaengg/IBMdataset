import math
N = int(input())
prime=[]
count=[]
ans = 1
place = 0
t=10**9
t+=7
for k in range(1,N+1):
    for i in range(2,k+1):
        while k % i == 0:
            k //= i
            if(i in prime):
                count[prime.index(i)] += 1
            else:
                prime.append(i)
                count.append(1)
                place += 1
for j in range(0,place):
    ans *= (count[j]+1)
print(ans%t)