X = input().strip()
A = [X[0]]
for i in range(1,len(X)):
    if X[i]=="T" and len(A)>0 and A[-1]=="S":
        A.pop()
    else:
        A.append(X[i])
print(len(A))