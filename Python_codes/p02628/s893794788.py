def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n,k=sep()
ar=lis()
ar.sort()
print(sum(ar[:k]))