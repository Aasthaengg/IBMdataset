n=int(input())
A=list(map(int,input().split()))
b=[0]*n
cnt=0
for i in range(n):
    if i%2==0:
        b[cnt]=A.pop()
        cnt+=1
    else:
        b[-cnt]=A.pop()

print(*b)