N = int(input())

A = 0
B = 0

result = 0
judg = 100000

for i in range(N-1):
    A = i + 1
    B = N - A
    for ii in range(len(str(A))):
        A_re = A % 10
        A = int(A / 10)
        result += A_re
    for iii in range(len(str(B))):    
        B_re = B % 10
        B = int(B / 10)
        result += B_re
    if judg>result:
        judg = result
    result = 0

print(judg)    


