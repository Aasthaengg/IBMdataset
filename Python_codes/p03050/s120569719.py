N=int(input())

sqrt_N = N**0.5

list_D=[]
list_A=[]

i=1
while(i<sqrt_N):
    if N%i == 0:
        list_D.append(i)
    i+=1

for d in list_D:
    list_A.append(N//d-1)
    
if N==1 or N==2:
    print(0)
else:
    if N%list_A[-1] == 0:
        list_A.pop(-1)
    print(sum(list_A))
