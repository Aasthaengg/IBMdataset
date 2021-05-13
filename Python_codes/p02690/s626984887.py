X = int(input())
for i in range(1,int(X**0.5)+1):
    if X%i==0:
        a = i
        b = X//i
        flag = 0
        for j in range(-1000,1000):
            B = j
            A = j+a
            if A**4+A**3*B+A**2*B**2+A*B**3+B**4==b:
                print(A,B)
                flag = 1
                break
        if flag==1:break
        a = X//i
        b = i
        flag = 0
        for j in range(1,1000):
            B = j
            A = j+a
            if A**4+A**3*B+A**2*B**2+A*B**3+B**4==b:
                print(A,B)
                flag = 1
                break