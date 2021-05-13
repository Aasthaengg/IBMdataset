W, a, b = map(int, input().split())

A2W = (a, a+W)
B2W = (b, b+W)

if (A2W[0] <= B2W[0] and B2W[0] <= A2W[1]) or (A2W[0] <= B2W[1] and B2W[1] <= A2W[1]):
    print(0)
elif B2W[0] > A2W[1]:
    print(B2W[0]-A2W[1])
else:
    print(A2W[0]-B2W[1])
