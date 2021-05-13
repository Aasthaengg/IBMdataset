n=int(input())
i=1
num=0
suml=[0]
while num<=10**7+1000:
    num+=i
    suml.append(num)
    i+=1

j=1
while n>suml[j]:
    j+=1
k=suml[j]-n
for ii in range(1,j+1):
    if ii!=k:
        print(ii)