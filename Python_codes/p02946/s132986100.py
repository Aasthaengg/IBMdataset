k,x=map(int,input().split(' '))

range1=(x-k)+1
range2=(x+k)-1

for i in range(range1,range2+1):
    print(i,end=' ')
