n=int(input())
L=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        L.append([i,n//i])
print(sum(L[-1])-2)