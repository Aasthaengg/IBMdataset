N,K=map(int,input().split())
kouho=[i for i in range(1,N+1)]
count = 0
i=0
while i+K<=N:
    count +=1
    i+=1

print(count)