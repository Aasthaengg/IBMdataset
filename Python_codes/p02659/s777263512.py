def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

a,b=input().strip().split(" ")
b=b.replace('.','')
b=int(b)
ans=int(a)*b
print(ans//100)