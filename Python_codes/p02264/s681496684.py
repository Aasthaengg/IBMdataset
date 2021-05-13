n,q = map(int, input().split())
a = []
t = 0
for i in range(n):
    a.append(input().split())
 
while len(a) != 0:
    A =  a.pop(0)
    if int(A[1]) <= q:
        t += int(A[1])
        print(A[0],t)
    else:
        t += q
        A[1] = int(A[1]) - q
        a.append(A)
