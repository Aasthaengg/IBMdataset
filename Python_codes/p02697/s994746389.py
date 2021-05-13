N,M = map(int, input().split())

M1 = M//2
M2 = M-M1

for i in range(M1):
    a=i+1
    b=2*M1+1-i
    print(a,b)
for i in range(M2):
    a=i+1
    b=2*M2-i
    print(2*M1+1 + a,2*M1+1 + b)