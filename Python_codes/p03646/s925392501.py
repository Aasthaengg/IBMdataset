K=int(input())

ini=(K//50)*50+49
A=[ini]*50
for i in range(K%50):
    A[i]+=50
add=K%50
for i in range(50):
    a=A[i]
    if a>ini:
        A[i]-=(K//50+1)*(add-1)+(K//50)*(50-add)
    else:
        A[i]-=(K//50+1)*(add)+(K//50)*(50-add-1)
print(50)
print(*A)