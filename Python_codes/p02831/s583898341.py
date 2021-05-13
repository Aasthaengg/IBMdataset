A,B=map(int,input().split())
num=1
for i in range(1,max(A,B)):
    if A%i==0 and B%i==0:
        num=i
print(int(A*B/num))