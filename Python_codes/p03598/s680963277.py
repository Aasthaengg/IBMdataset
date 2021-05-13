N = int(input())
K = int(input())
x = list(map(int, input().split()))

A=[]
B=[]

for i in range(len(x)):
    a = min(2*(x[i]), 2*abs(K-x[i]))
    A.append(a)

print(sum(A))