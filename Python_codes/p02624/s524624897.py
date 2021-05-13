import math , sys

N = int(input())
Ns = int(math.sqrt(N))+1
if N == 1:
    print(1)
    sys.exit()
if N == 2:
    print(5)
    sys.exit()
if N == 3:
    print(11)
    sys.exit()
if N == 4:
    print(23)
    sys.exit()
if N == 5:
    print(33)
    sys.exit()  

ans = [ 2 for _ in range(N+1)]
ans[0]=0
ans[1]=1
for i in range(2,Ns):
    num=i
    while num < N+1:
        if math.sqrt(num)<i:
            flag=True
        elif num == i**2:
            ans[num]+=1
        else:
            ans[num]+=2
        num+=i
tot = 0
for i in range(N+1):
    tot+=i*ans[i]
print(tot)