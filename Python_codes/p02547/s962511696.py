def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


n=int(input())
ar=[]
for i in range(n):
    a,b=sep()
    if a==b:
        ar.append(1)
    else:
        ar.append(0)


for i in range(2,n):
    if ar[i]==1 and ar[i-1]==1 and ar[i-2]==1:
        print("Yes")
        quit()
print("No")

