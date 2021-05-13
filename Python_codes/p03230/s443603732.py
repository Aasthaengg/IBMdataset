n=int(input())

num=0
for i in range(1,10**3):
    if i*(i-1)//2==n:
        num=i
        break

if num==0:print("No");exit()
length=num-1
A,cnt=[],1
for i in range(1,num):
    B=[]
    cnt +=i-1
    for j in range(i):B.append(cnt+j)
    for j in range(i,length):B.append(B[-1]+j)
    A.append(B)
A.append([i*(i+1)//2 for i in range(1,length+1)])

print("Yes")
print(length+1)
for i in A:
    print(length,*i)