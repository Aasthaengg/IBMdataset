n=int(input())
def div(h):
    y=[]
    for i in range(1,int(h**0.5)+1):
        if n%i==0:
            y.append((i,n//i))
    m=float("inf")
    for a,b in y:
        m=min(m,a+b-2)
    return m
print(div(n))