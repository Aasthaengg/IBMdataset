n=int(input())
t,a=map(int,input().split())
h=list(map(int, input().split()))
li=[]
for i in range(n):
    temp1=t-h[i]*6/1000
    temp2=abs(a-temp1)
    li+=[(i+1,temp2)]
li.sort(key=lambda x:(x[1]))
print(li[0][0])