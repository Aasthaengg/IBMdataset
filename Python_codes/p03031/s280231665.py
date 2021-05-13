N,M=map(int,input().split())
lights=[]
for _ in range(M):
    number=list(map(int,input().split()))
    lights.append(number[1:])
p=list(map(int,input().split()))
switches=[n for n in range(1,N+1)]
kouho=[]
n=len(switches)
for i in range(2**n):
    switch=[]
    for j in range(n):
        if ((i>>j)&1):
            switch.append(switches[j])
    kouho.append(switch)
del kouho[0]
ans=0
for kou in kouho:
    numbers=[0 for _ in range(M)]
    for k in kou:
        for n in range(M):
            if k in lights[n]:
                numbers[n]+=1
    for n in range(M):
        numbers[n]=numbers[n]%2
    if numbers==p:
        ans+=1
if p ==[0 for _ in range(M)]:
    ans+=1
print(ans)
