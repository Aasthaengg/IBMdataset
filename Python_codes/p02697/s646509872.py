N,M = map(int,input().split())

a = 0
b = M+1

for i in range(M//2):
    a += 1
    b -= 1
    print(a,b)

a = M
b = 2*M+2

for i in range((M+1)//2):
    a += 1
    b -= 1
    print(a,b)
