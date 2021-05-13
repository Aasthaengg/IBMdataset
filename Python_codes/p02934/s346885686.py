l1=list()
n=int(input())
l1+=list(map(int,input().split(' ')))
f=0
for i in range(len(l1)):
    f+=(1/l1[i])
print(1/f)

