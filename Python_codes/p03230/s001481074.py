n = int(input())
k = int((n*2)**(1/2))-1
for i in range(10):
    if (k+i)*(k+i-1)==n*2:
        k+=i
        break
if k*(k-1)!=n*2:
    print("No")
    exit()
print("Yes")
print(k)
tri = []

for i in range(1,k):
    tri.append([j for j in range(i*(i-1)//2+1,i*(i+1)//2+1)])
for i in range(k-1):
    print(k-1,end = " ")
    print(*tri[i],end=" ")
    for j in range(i+1,k-1):
        print(tri[j][i],end=" ")
    print()
print(k-1,end=" ")    
for i in range(k-1):
    print(tri[i][-1],end = " ")

