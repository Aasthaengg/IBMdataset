a,b,k = map(int,input().split())
num=[]
for i in range(100):
    if(a%(i+1) == 0 and b%( i+1)==0):
        num.append(str(i+1))
x = len(num)
#print("num:"+str(num))
#print("x:"+ str(x))
print(num[x-k])