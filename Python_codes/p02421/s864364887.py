n=int(input())
T=0
H=0
for i in range(n):
    [a,b]=input().split(" ")
    if(a>b):
        T+=3
    elif(a<b):
        H+=3
    else:
        T+=1
        H+=1
print(str(T)+" "+str(H))