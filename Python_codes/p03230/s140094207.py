n=int(input())

flag,length=0,0
for i in range(1,10**3):
    if n==i*(i+1)//2:
        flag,length=1,i
        break
if not flag:print("No");exit()

A=[]
for i,j in enumerate(range(1,length+1)):
    num=j*(j+1)//2
    B=[]
    for k in range(i):
        B.append(num-(k+1))
    point=i+1
    B.append(num)
    for k in range(length-(i+1)):
        B.append(B[-1]+point)
        point +=1
    A.append(B)
A.append([i*(i+1)//2 for i in range(1,length+1)])

print("Yes")
print(len(A))
for i in A:
    print(length,*i)