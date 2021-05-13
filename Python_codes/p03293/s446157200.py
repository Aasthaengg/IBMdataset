#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

s=list(input())
t=list(input())

n=len(s)
flag=False

for i in range(n):
    last=s.pop()
    s.insert(0,last)
    #print(s)
    if s==t:
        flag=True
        break

if flag:
    print("Yes")
else:
    print("No")