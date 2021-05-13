N = int(input())
b = 0
c = 0
first = 0
A = []
for i in range(N):
    a = int(input())
    if b < a:
        ind = i
        b = a
    A.append(a)
for j in range(N):
    if j==ind:
        continue
    if c < A[j]:
        sind = j
        c = A[j]
for k in range(N):
    if k==ind:
        print(c)
    else:
        print(b)
