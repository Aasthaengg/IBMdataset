A = []
for i in range(5):
    a=int(input())
    A.append(a)
A.sort()
k = A[4] - A[0]
K = int(input())
if k<=K:
    print("Yay!")
else:
    print(":(")