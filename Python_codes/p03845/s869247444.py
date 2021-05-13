n=int(input())
t=[int(i)for i in input().split()]
m=int(input())
drink=[[int(i)for i in input().split()]for j in range(m)]

for i in range(m):
    tmp=t[:]
    tmp[drink[i][0]-1]=drink[i][1]
    print(sum(tmp))
