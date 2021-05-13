n=int(input())
cnt=0

def digit(k):
    ret=0
    while k!=0:
        k//=10
        ret+=1
    return ret
    
for i in range(n):
    if digit(i+1)%2==1: cnt+=1
print(cnt)