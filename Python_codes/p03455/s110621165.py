A = list(map(int, input().split()))
p = A[0]*A[1]
if p%2 == 0:
    print("Even")
else:
    print("Odd")