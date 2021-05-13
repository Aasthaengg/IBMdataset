num = [int(e) for e in input().split()]
A=num[0]
B=num[1]
if B%A==0:
    print(A+B)
else:
    print(B-A)