N=int(input())

A= [(-2)**i for i in range(40)]
#print(A)
ans=""

for i,num in enumerate(A):
    if N%((-2)**(i+1))==0:
        ans += "0"
    else:
        ans += "1"
        N -= num
    if N==0:
        break
print(ans[::-1])