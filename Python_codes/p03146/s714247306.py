s = int(input())

A = []
A.append(s)

while True:
    if s%2 == 0:
        s = s//2
    else:
        s = 3*s+1
    if s in A:
        print(len(A)+1)
        break
    else:
        A.append(s)