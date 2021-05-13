N = int(input())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
a,b = A[-1]
print(a+b)