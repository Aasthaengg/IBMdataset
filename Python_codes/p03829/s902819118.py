z=list(map(int,input().split()))
X=list(map(int,input().split()))
N,A,B=z[0],z[1],z[2]
a=1
p=0
while True:
    p+=min((X[a]-X[a-1])*A,B)
    a+=1
    if a==N:
        break
print(p)