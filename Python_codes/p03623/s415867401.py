A=list(map(int, input().split()))
x=A[0]
a=A[1]
b=A[2]

if abs(x-a)<abs(x-b):
    print("A")
else:
    print("B")