

n=int(input())
a=list(map(int,input().split()))
li=[0]*n

for i in range(n-1):
    t=a[i]
    li[t-1]+=1

for i in range(n):
    print(li[i])



        
