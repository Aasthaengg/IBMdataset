s=[2]
a=[int(i) for i in range(2,10000) if pow(2 ,int(i)-1, int(i)) ==1]

while a!=[]:
    t=a[0]
    a=[i for i in a if i % t !=0]
    s.append(t)

n=int(input())
x=0
for i  in range(n):
    y=0
    t = int(input())
    for j in s:
        if t % j ==0 and t !=j:
           break
    else:
        x+=1
print(x)