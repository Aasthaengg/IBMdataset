n=int(input())

def sum0f(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

list=[]    
for a in range(1,n):
    list.append(sum0f(a)+sum0f(n-a))
    
print(min(list))
