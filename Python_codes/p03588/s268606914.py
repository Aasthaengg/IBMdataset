N = int(input())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
a = A[-1][0]
b = A[-1][1]
print(a+b)