X = int(input())
A = []
k=20
for i in range(1,int(X**0.5)+1):
    for j in range(k):
        if i**j<=X:
            A.append(i**j)
        elif i++j > X:
            k = j+1
            break
print(max(A))
