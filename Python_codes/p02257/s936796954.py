#ALDS1_1-C Prime Numbers
def prime(n):
    s=3
    while(s*s <= n):
        if(n%s==0):
            return False
        s+=2
    return True

n=int(input())
num=0
for i in range(n):
    x = int(input())
    if prime(x) and x%2!=0:
        num+=1
    if x==2:
        num+=1
print(num)