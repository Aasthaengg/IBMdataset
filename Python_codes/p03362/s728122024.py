n=int(input())

X=[]

def j(n):
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

for i in range(2,55556):
    if j(i) and i%5==1:
        X.append(i)

print(*X[:n])










