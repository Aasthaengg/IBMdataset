price,ticket=[],[]
A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(M):
    ticket.append(list(map(int,input().split())))
price.append(min(a)+min(b))
for i in range(M):
    price.append(a[ticket[i][0]-1]+b[ticket[i][1]-1]-ticket[i][2])
print(min(price))