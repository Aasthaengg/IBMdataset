N=int(input())
L=sorted(list(map(int,input().split())))
count=0
for i in range(0,N-1):
    count+=L[i]
if L[N-1]<count:
    print("Yes")
else:
    print("No")