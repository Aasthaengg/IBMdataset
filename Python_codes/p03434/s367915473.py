N = int(input())
A = sorted(list(map(int,input().split())), reverse = True)
a = 0 
b = 0
for i in range(len(A)):
    if i%2 == 0:
        a += A[i]
    else:
        b += A[i]
print(a-b)