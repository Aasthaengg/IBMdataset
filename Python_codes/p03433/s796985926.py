N = int(input())
A = int(input())
flag=0
for i in range(10001):
    for j in range(A+1):
        if N==500*i+j:
            flag=1
if flag==0:
    print("No")
else:
    print("Yes")