flag = [False]*100001
c = [0]*100002
n = int(input())

for i in range(2,100000):
    if(not(flag[i])):
        for j in range(i+i,100000,i):
            flag[j] = True

for i in range(3,100000,2):
    if(not(flag[i]) and not(flag[(i+1)//2])):
        c[i]+=1
for i in range(3,100000):
    c[i]+=c[i-1]

while(n):
    n-=1
    l,r = map(int,input().split())
    print(c[r]-c[l-1])