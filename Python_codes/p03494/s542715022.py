# 081B
N = int(input())
A = list(map(int, input().split())) 
c = 0
b = 0
while True:
    for i in range(N):
        if (A[i]%2) == 0:
            A[i] = A[i]/2
        else:
            c =1
            break
    if c == 1:
        break
    b += 1
    
print(b)