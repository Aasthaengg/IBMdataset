X = int(input())
A = int(input())
B = int(input())

C = X-A
n = 1

while (C >= B):
    C -= B*n
    if (C >= B):
        C = X-A
        n += 1
    else:
        print(C)