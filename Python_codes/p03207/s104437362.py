a=int(input())
b=[0]*a
for i in range(a):
    b[i]=int(input())
print(int(sum(b)-max(b)//2))