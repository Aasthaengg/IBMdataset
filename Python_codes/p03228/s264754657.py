a,b,k=map(int,input().split())
def rule(a,b):
    if a%2==0:
        return a//2,b+a//2     
    else:
        return (a-1)//2,b+(a-1)//2

for i in range(k):
    if i%2==0:
        a,b=rule(a,b)
    else:
        b,a=rule(b,a)
print(a,b)