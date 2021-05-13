N,M=map(int,input().split())
temp=0
TEMP=N-1
for i in range(M):
    a,b=map(int,input().split())
    if b-1<temp or TEMP<a-1:
        print(0)
        exit()
    if a-1>temp:
        temp=a-1
    if TEMP>b-1:
        TEMP=b-1
    
print(TEMP-temp+1)
