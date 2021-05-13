x=[]
y=[]
result=[]
num=input().split(' ')
for i in range(0,int(num[0]),1):
    num1=input().split(' ')
    x.append(num1)
for j in range(0,int(num[1]),1):
    num2=input().split(' ')    
    y.append(num2)
for k in range(0,int(num[0]),1):
    a=[]
    for j in range(0,int(num[2]),1):
        a.append(0)
    result.append(a)    
for i in range(len(x)):  
   for j in range(len(y[0])):  
       for k in range(len(y)):  
            result[i][j] +=int(x[i][k]) * int(y[k][j])
for r in range(0,int(num[0]),1):
    for j in range(0,int(num[2]),1):
        if j==int(num[2])-1:
            print(result[r][j])
        else:    
           print(result[r][j],end=" ")
    if r==int(num[0])-1:
        break
    
