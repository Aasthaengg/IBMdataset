from math import sqrt

N = int(input())
ans = 0
for M in range(105,N+1,1):
    if M%2==0:
        continue 
    count=0
    for i in range(1,int(sqrt(M))+2,1):
        if M % i ==0:
            if M % i == 0:
                count+=2
    if count==8:
        ans+=1
print(ans)