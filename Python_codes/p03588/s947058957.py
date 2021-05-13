N=int(input())
num=[]
for i in range(N):
    a,b=map(int,input().split())
    num.append((a,b))

num=sorted(num)[::-1]

x=num[0][0]
y=num[0][1]

print(x+y)