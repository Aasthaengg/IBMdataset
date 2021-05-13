inp=input().split(" ")
H=int(inp[0])
W=int(inp[1])
N=int(inp[2])
plot=[]
times=[0 for i in range(10)]
times[0]=(H-2)*(W-2)
from collections import defaultdict
count=defaultdict(lambda:0)
def check(a,b,count):
    for i in range(3):
        for j in range(3):
            if a-i>=0 and b-j>=0 and a+2-i<=H-1 and b+2-j<=W-1:
                count[str([a-i,b-j])]+=1
for i in range(N):
    plot.append(list(map(int,input().split(" "))))
    check(plot[i][0]-1,plot[i][1]-1,count)
for i in count.values():
    times[i]+=1
    times[0]-=1
for i in range(len(times)):
    print(times[i])