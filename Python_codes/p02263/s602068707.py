A = list(input().split())
B = []

for i in range(len(A)):
    if A[i]=='+':
        y=B.pop()
        x=B.pop()
        B.append(x+y)
    elif A[i]=='-':
        y=B.pop()
        x=B.pop()
        B.append(x-y)
    elif A[i]=='*':
        y=B.pop()
        x=B.pop()
        B.append(x*y)
    else:
        B.append(int(A[i]))

print(B[0])
