K = int(input())
N = 50
X = K//N
Y = K%N
B = N-1+X-Y
print(N)
print(*[B+N+1 if i<Y else B for i in range(N)])