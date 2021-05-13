ryuka = [0]*87

ryuka[0]=2
ryuka[1]=1
for i in range(2,87,1):
    ryuka[i]=ryuka[i-1]+ryuka[i-2]

N = int(input())

print(ryuka[N])