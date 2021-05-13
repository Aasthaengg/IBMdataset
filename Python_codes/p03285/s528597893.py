N=int(input())

flag=False
for i in range(100):
    if ((N-4*i)%7==0) and ((N-4*i)/7>=0):
        flag=True
print("Yes" if flag else "No")
