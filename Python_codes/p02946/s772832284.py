k,x=map(int,input().split())
mi=max(-1000000,x-k+1)
ma=min(1000000,x+k-1)
a=[]
for i in range(0,ma-mi+1):
    a.append(i+mi)
print(*a)