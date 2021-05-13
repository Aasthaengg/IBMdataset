A=list(map(int,input().split()))
a=A[0]
b=A[1]
count=0
i=1
while i<b:
    count=count+1
    i=i+a-1
print(count)