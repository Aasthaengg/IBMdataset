n=int(input())
trans=[0]*5
for i in range(5):
    trans[i]=int(input())
print(-(-n//min(trans))+4)