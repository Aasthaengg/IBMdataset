N = int(input())
if N == 1:
    print("Hello World")
elif N == 2:
    A=[]
    for i in range(2):
        add = int(input())
        A.append(add)
    print(sum(A))