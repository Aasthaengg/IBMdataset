x=[]
y=[]
count=0
while True:
    i,j=map(int,raw_input().split())
    if (i,j)==(0,0):
        break
    count+=1
    x.append(i)
    y.append(j)

for i in range(count):
    print('#'*y[i])
    for j in range(x[i]-2):
        print('#'+'.'*(y[i]-2)+'#')
    if x[i]!=1:    
        print('#'*y[i])
    print('')