from sys import stdin
N,k1,k2=[int(x) for x in stdin.readline().rstrip().split()]
a = []
for i in range(N):
    a.append([int(x) for x in stdin.readline().rstrip().split()])
cnt=0
for i in a:
    tmp1=i[0]-k1
    tmp2=i[1]-k2
    if tmp1>=0 and tmp2>=0:
        cnt+=1
print(cnt)