A = list(input().split())
if A[0] == A[1]:
    print("=")
elif min(A[0],A[1]) == A[1]:
    print(">")
else:
    print("<")