N=int(input())
a=[]
b=[]
for c in range(N):
    A,B=map(int,input().split())
    a.append(int(A))
    b.append(int(B))
newa=sorted(a)
newb=sorted(b)
number=N
for c in range(N-1):
    z=newa[c+1]-newa[c]-1
    number+=z
y=newa[0]-1
number+=y
number+=newb[0]
print(number)
