N=int(input())
m=1
while m*(m+1)<2*N:m+=1
for i in range(1,m+1):
    if m*(m+1)//2-i!=N:print(i)
