n,m,d=map(int, input().split(" "))
if d==0:
    node=n
else:
    if n<2*d:
        node=n
    else:
        node1=2*d
        node2=n-2*d
        node=node1*1+node2*2
print(node/(n**2)*(m-1))
