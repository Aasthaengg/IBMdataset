X = int(input())
A = []
for i in range(1,X+1):
    for j in range(2,100):
        if i**j > X:
            break
        A.append(i**j)
print(max(A))