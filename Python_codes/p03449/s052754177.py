Input=[list(map(int,s.split())) for s in open(0)]
NN=Input[0]
N=NN[0]
A1=Input[1]
A2=Input[2]
canlist=[]
for i in range(N):
    candy=0
    candy+=sum(A1[:i+1])
    candy+=sum(A2[i:])
    canlist.append(candy)
print(max(canlist))